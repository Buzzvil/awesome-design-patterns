class Helicopter(override val mediator: Mediator): Component {
    fun notifyPassthrough(){
        this.mediator.notify(sender=this, event=Event.PASS_THROUGH)
    }
}