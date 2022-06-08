fun someClientCode(handler: Handler, requestContent: String) {
    val result = handler.handle(requestContent)
    println("\"$requestContent\": $result")
}

fun main(args: Array<String>) {
    val authentication = AuthenticationHandler()
    val authorization = AuthorizationHandler()
    val validation = ValidationHandler()
    authentication
        .setNext(authorization)
        .setNext(validation)

    val authenticatedOnlyRequest = "only authenticated"
    println("Chain: Authentication ✅ -> Authorization ❌")
    someClientCode(handler = authentication, requestContent = authenticatedOnlyRequest)
    println()

    val allPassRequest = "authenticated and authorized and validated"
    println("Chain: Authentication ✅ -> Authorization ✅ -> Validation ✅")
    someClientCode(handler = authentication, requestContent = allPassRequest)
}