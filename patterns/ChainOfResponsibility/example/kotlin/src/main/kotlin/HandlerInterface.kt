interface HandlerInterface {
    fun setNext(handler: Handler): Handler

    fun handle(request: String): String
}