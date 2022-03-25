interface Handler {
    fun setNext(handler: Handler): Handler

    fun handle(request: String): String?

    var nextHandler: Handler?
}