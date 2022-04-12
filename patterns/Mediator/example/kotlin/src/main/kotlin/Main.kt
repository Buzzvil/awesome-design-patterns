fun main(args: Array<String>) {
    val mediator = ControlTower()

    val glider = Glider(mediator)
    val helicopter = Helicopter(mediator)
    val airplane = Airplane(mediator)

    glider.notifyTakeOff()
    helicopter.notifyPassthrough()
    airplane.notifyLanding()
}