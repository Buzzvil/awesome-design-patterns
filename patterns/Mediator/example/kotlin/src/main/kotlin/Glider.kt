class Glider(override val mediator: Mediator, override val sender: Sender=Sender.GLIDER): Component {
    fun notifyTakeOff(){
        this.mediator.notify(this.sender, Event.TAKE_OFF)
    }
}