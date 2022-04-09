class Airplane(override val mediator: Mediator): Component {
    fun notifyLanding(){
        this.mediator.notify(sender=this, event=Event.LANDING)
    }

    override fun doIt(event: Event) {
        if (event == Event.LANDING) {
            print("landing")
        }
    }

    override fun dontDoThat(event: Event) {
        if (event == Event.LANDING) {
            print("waiting for landing")
        }
    }
}