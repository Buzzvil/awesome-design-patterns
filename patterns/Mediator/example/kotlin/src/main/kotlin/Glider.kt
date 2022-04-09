class Glider(override val mediator: Mediator): Component {
    fun notifyTakeOff(){
        this.mediator.notify(sender=this, event=Event.TAKE_OFF)
    }
}