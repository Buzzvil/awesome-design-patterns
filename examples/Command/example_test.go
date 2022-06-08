package command

import "testing"

func TestSlackCommand(t *testing.T) {
	services := []Receiver{newAllocationService(), newBudgetThrottlingService()}
	target := "dev"
	user := "nathan.yang"

	for _, service := range services {
		checkCmd := newCheckCommand(service)
		invoker := newSlack(checkCmd)

		invoker.executeCommand()
		if service.status[target] != "" {
			t.Fail()
		}

		checkoutCmd := newCheckoutCommand(service, target, user)
		checkoutInvoker := newSlack(checkoutCmd)
		checkoutInvoker.executeCommand()

		if service.status[target] != user {
			t.Fail()
		}
	}
}

func TestDirectExecuteCommand(t *testing.T) {
	services := []Receiver{newAllocationService(), newBudgetThrottlingService()}
	target := "dev"
	user := "nathan.yang"

	for _, service := range services {
		checkCmd := newCheckCommand(service)
		invoker := newDirectExecute(checkCmd)

		invoker.executeCommand()
		if service.status[target] != "" {
			t.Fail()
		}

		checkoutCmd := newCheckoutCommand(service, target, user)
		checkoutInvoker := newDirectExecute(checkoutCmd)
		checkoutInvoker.executeCommand()

		if service.status[target] != user {
			t.Fail()
		}
	}
}
