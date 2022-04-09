class Airplane(override val mediator: Mediator, override val sender: Sender=Sender.AIRPLANE): Component {
    fun notifyLanding(){
        this.mediator.notify(this.sender, Event.LANDING)
    }
}