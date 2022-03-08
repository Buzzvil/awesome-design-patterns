// This interpreter just check if the data is same as the interpreter data.
class TerminalExpression(expressionData: String): Expression {
    private val expressionData = expressionData

    override fun interpreter(data: String): Boolean = this.expressionData == data
}