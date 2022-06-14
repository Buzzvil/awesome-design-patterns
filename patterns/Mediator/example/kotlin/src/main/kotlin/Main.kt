fun main(args: Array<String>) {
    val mediator = ControlTower()

    val glider = Glider(mediator)
    val helicopter = Helicopter(mediator)
    val airplane = Airplane(mediator)

    glider.notifyTakeOff()
    // glider: start taking off

    helicopter.notifyPassthrough()
    // helicopter: passing through

    airplane.notifyLanding()
    // airplane: waiting for landing
}