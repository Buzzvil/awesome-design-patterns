class Helicopter(override val mediator: Mediator): Component {
    fun notifyPassthrough(){
        this.mediator.notify(sender=this, event=Event.PASS_THROUGH)
    }

    override fun doIt(event: Event) {
        if (event == Event.PASS_THROUGH) {
            print("passing through")
        }
    }

    override fun dontDoThat(event: Event) {
        if (event == Event.PASS_THROUGH) {
            print("turning around")
        }
    }
}