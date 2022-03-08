class AndExpression(expression1: Expression, expression2: Expression): Expression {
    private val expression1 = expression1
    private val expression2 = expression2

    override fun interpreter(data: String): Boolean {
        return this.expression1.interpreter(data) && this.expression2.interpreter(data)
    }
}