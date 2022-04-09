class ControlTower: Mediator {
    override fun notify(sender: Sender, event: Event) {
        print(sender)
    }
}