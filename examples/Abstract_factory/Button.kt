interface Button {
    val backgroundColor: Color
    val text: String

    fun onClick()
}

class LightThemeButton(
    override val text: String
): Button {
    override val backgroundColor: Color = Color.WHITE

    override fun onClick() {
        println("Light theme button clicked: $text, $backgroundColor")
    }
}

class DarkThemeButton(
    override val text: String
): Button {
    override val backgroundColor: Color = Color.BLACK

    override fun onClick() {
        println("Dark theme button clicked: $text, $backgroundColor")
    }
}
