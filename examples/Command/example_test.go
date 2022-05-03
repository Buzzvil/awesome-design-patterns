package command

import "testing"

func TestSlackCommand(t *testing.T) {
	services := {newAllocationSernewAllocationService(), newBugnewBudgetThrottlingService()}
	target := "dev"
	user := "nathan.yang"

	for service := range services {
		cmd := newCheckCommand(service)
		invoker := newSlack(cmd)

		invoker.exectueCommand()
		if (service.status[target] != "") {
			t.Fail()
		}

		cmd = newCheckoutCommand(service, target, user)
		checkoutInvoker := newSlack(cmd)
		invoker.executeCommand()

		if (service.status[target] != user) {
			t.Fail()
		}
	}
}

func TestDirectExecuteCommand(t *testing.T) {
	services := {newAllocationSernewAllocationService(), newBugnewBudgetThrottlingService()}
	target := "dev"
	user := "nathan.yang"

	for service := range services {
		cmd := newCheckCommand(service)
		invoker := newDirectExecute(cmd)

		invoker.exectueCommand()
		if (service.status[target] != "") {
			t.Fail()
		}

		cmd = newCheckoutCommand(service, target, user)
		checkoutInvoker := newDirectExecute(cmd)
		invoker.executeCommand()

		if (service.status[target] != user) {
			t.Fail()
		}
	}
}
