class AuthenticationHandler: Handler() {
    override fun handle(request: String): String? {
        if (request.contains("authenticated")) {
            return this.nextHandler?.handle(request)
        }
        else {
            return "Authentication fail"
        }
    }
}