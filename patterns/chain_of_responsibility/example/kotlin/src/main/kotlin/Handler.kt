open class Handler: HandlerInterface {
    var nextHandler: Handler? = null

    override fun handle(request: String): String? {
        print("called handle with request:" + request)
        return nextHandler?.handle(request)
    }

    override fun setNext(handler: Handler): Handler {
        this.nextHandler = handler
        return handler
    }
}
