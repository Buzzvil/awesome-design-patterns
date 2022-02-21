interface UiComponentFactory {
    fun createButton(text: String): Button
    fun createTextView(text: String): TextView
}

class LightThemeUIComponentFactory: UiComponentFactory {
    override fun createButton(text: String): Button {
        return LightThemeButton(text)
    }

    override fun createTextView(text: String): TextView {
        return LightThemeTextView(text)
    }
}

class DarkThemeUIComponentFactory: UiComponentFactory {
    override fun createButton(text: String): Button {
        return DarkThemeButton(text)
    }

    override fun createTextView(text: String): TextView {
        return DarkThemeTextView(text)
    }
}
