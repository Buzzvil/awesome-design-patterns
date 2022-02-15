interface TextView {
    val backgroundColor: Color
    val textColor: Color
    val text: String

    fun printText()
}

class LightThemeTextView(
    override val text: String
): TextView {
    override val backgroundColor: Color = Color.WHITE
    override val textColor: Color = Color.BLACK

    override fun printText() {
        println("Light theme text view: $text")
    }
}

class DarkThemeTextView(
    override val text: String
): TextView {
    override val backgroundColor: Color = Color.BLACK
    override val textColor: Color = Color.WHITE

    override fun printText() {
        println("Dark theme text view: $text")
    }
}
