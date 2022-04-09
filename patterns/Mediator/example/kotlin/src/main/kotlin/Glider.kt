class Glider(override val mediator: Mediator): Component {
    fun notifyTakeOff(){
        this.mediator.notify(sender=this, event=Event.TAKEOFF)
    }

    override fun doIt(event: Event): Unit {
        if (event == Event.TAKEOFF) {
            print("start taking off")
        }
    }

    override fun dontDoThat(event: Event) {
        if (event == Event.TAKEOFF) {
            print("waiting for takeoff")
        }
    }
}