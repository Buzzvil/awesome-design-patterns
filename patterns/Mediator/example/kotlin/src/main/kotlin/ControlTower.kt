class ControlTower: Mediator {
    override fun notify(sender: Component, event: Event): Unit {
        when (event) {
            Event.LANDING -> sender.dontDoThat(event)
            Event.PASS_THROUGH -> sender.doIt(event)
        }
    }
}