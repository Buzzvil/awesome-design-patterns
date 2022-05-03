open class Handler: HandlerInterface {
    var nextHandler: Handler? = null

    override fun handle(request: String): String {
        return nextHandler?.handle(request) ?: "Completed!"
    }

    override fun setNext(handler: Handler): Handler {
        this.nextHandler = handler
        return handler
    }
}
