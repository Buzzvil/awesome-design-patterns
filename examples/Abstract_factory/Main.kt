fun main(args: Array<String>) {
    // 사용자 입력에 따라서 라이트 or 다크 테마 UI 컴포넌트 생성
    println("light or dark?")
    val factory = when (readLine()!!) {
        "light" -> LightThemeUIComponentFactory()
        "dark" -> DarkThemeUIComponentFactory()
        else -> throw IllegalArgumentException("light 또는 dark만 입력")
    }

    val button = factory.createButton("버튼!")
    val textView = factory.createTextView("텍스트뷰!")

    button.onClick()
    textView.printText()

    // 실행 예시

    /*
    light or dark?
    >> light
    Light theme button clicked: 버튼!, java.awt.Color[r=255,g=255,b=255]
    Light theme text view: 텍스트뷰!
    */

    /*
    light or dark?
    >> dark
    Dark theme button clicked: 버튼!, java.awt.Color[r=0,g=0,b=0]
    Dark theme text view: 텍스트뷰!
    */

    /*
    light or dark?
    >> ㅁㄴㅇㄹ
    Exception in thread "main" java.lang.IllegalArgumentException: light 또는 dark만 입력
        at MainKt.main(Main.kt:9)
    */
}
