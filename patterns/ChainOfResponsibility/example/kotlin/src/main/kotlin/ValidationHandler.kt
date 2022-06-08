class ValidationHandler: Handler() {
    override fun handle(request: String): String {
        if (request.contains("validated")) {
            return super.handle(request)
        }
        else {
            return "Validation fail"
        }
    }
}