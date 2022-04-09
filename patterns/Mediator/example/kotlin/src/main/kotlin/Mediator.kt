interface Mediator {
    fun notify(sender: Component, event: Event): Unit
}