class ControlTower: Mediator {
    override fun notify(sender: Component, event: Event) {
        print(sender)
    }
}