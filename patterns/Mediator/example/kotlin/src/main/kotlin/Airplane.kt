class Airplane(override val mediator: Mediator): Component {
    fun notifyLanding(){
        this.mediator.notify(sender=this, event=Event.LANDING)
    }
}