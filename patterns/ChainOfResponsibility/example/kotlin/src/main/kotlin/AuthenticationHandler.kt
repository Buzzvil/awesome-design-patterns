class AuthenticationHandler: Handler() {
    override fun handle(request: String): String {
        if (request.contains("authenticated")) {
            return super.handle(request)
        }
        else {
            return "Authentication fail"
        }
    }
}