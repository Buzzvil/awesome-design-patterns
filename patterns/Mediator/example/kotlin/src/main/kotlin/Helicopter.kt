class Helicopter(override val mediator: Mediator, override val sender: Sender=Sender.HELICOPTER): Component {
    fun notifyPassthrough(){
        this.mediator.notify(this.sender, Event.PASS_THROUGH)
    }
}