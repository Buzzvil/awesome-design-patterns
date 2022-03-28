class AuthorizationHandler: Handler() {
    override fun handle(request: String): String {
        if (request.contains("authorized")) {
            return super.handle(request)
        }
        else {
            return "Authorization fail"
        }
    }
}