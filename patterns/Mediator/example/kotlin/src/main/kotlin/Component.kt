interface Component {
    val mediator: Mediator
    fun dontDoThat(event: Event): Unit
    fun doIt(event: Event): Unit
}