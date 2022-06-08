package command

import "fmt"

/*
Invoker
- Slack
- DirectExecute
Command
- CheckCommand
- CheckoutCommand
- CheckinCommand
Receiver
- AllocationService
- BudgetThrottlingService
*/

type Invoker interface {
	setCommand(Command)
	executeCommand()
}

type Slack struct {
	cmd  Command
	name string
}

type DirectExecute struct {
	cmd  Command
	name string
}

type Command interface {
	execute()
	name() string
}

type CommandBase struct {
	name string
}

func (c CommandBase) getName() string {
	return c.name
}

type CheckCommand struct {
	CommandBase
	receiver Receiver
}

type CheckoutCommand struct {
	CommandBase
	receiver Receiver
	target   string
	user     string
}

type Receiver struct {
	name   string
	status map[string]string
}

func newSlack(cmd Command) Slack {
	return Slack{cmd: cmd, name: "Slack"}
}

func (s Slack) setCommand(cmd Command) {
	fmt.Printf("Setting Slack command as %s", cmd.name())
	s.cmd = cmd
}

func (s Slack) executeCommand() {
	fmt.Printf("Executing Slack command %s", s.cmd.name())
	s.cmd.execute()
}

func newDirectExecute(cmd Command) DirectExecute {
	return DirectExecute{cmd: cmd, name: "DirectExecute"}
}

func (d DirectExecute) setCommand(cmd Command) {
	fmt.Printf("Setting DirectExecute command as %s", cmd.name())
	d.cmd = cmd
}

func (d DirectExecute) executeCommand() {
	fmt.Printf("Executing DirectExecute command %s", d.cmd.name())
	d.cmd.execute()
}

func newCheckCommand(receiver Receiver) CheckCommand {
	return CheckCommand{CommandBase{name: "CheckCommand"}, receiver}
}

func newCheckoutCommand(receiver Receiver, target string, user string) CheckoutCommand {
	return CheckoutCommand{CommandBase{name: "CheckoutCommand"}, receiver, target, user}
}

func (c CheckCommand) execute() {
	s := c.receiver.status
	for env, occupier := range s {
		fmt.Printf("%s: %s", env, occupier)
	}
}

func (c CheckCommand) name() string {
	return c.getName()
}

func (c CheckoutCommand) execute() {
	s := c.receiver.status
	s[c.target] = c.user
	fmt.Printf("%s occupied %s!", c.user, c.target)
}

func (c CheckoutCommand) name() string {
	return c.getName()
}

func newAllocationService() Receiver {
	return Receiver{name: "AllocationService", status: map[string]string{}}
}

func newBudgetThrottlingService() Receiver {
	return Receiver{name: "BudgetThrottlingService", status: map[string]string{}}
}
