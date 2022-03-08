import io.kotest.core.spec.style.BehaviorSpec
import kotlin.test.assertEquals

class TerminalExpressionSpec: BehaviorSpec({
    given("banana 라는 context 를 가진 TerminalExpression 이 있다.") {
        val bananaTerminalExpression = TerminalExpression("banana")

        `when` ("context 와 동일한 data 가 주어진다.") {
            val data = "banana"

            then("interpreter 는 context 와 data가 같은 경우 true 를 반환해야 한다") {
                val result = bananaTerminalExpression.interpreter(data)
                assertEquals(true, result)
            }
        }

        `when` ("context 와 다른 data 가 주어진다.") {
            val data = "apple"

            then("interpreter 는 context 와 data가 다른 경우 false 를 반환해야 한다") {
                val result = bananaTerminalExpression.interpreter(data)
                assertEquals(false, result)
            }
        }
    }

})

class ExpressionSpec: BehaviorSpec({
    given("2개의 과일이 있다.") {
        val fruit1 = TerminalExpression("apple")
        val fruit2 = TerminalExpression("banana")

        `when` ("OrExpression 을 통해 isSingle 이라는 interpreter 를 만들었다.") {
            val isSingle = OrExpression(fruit1, fruit2)

            then("이래야 한다.") {
                assertEquals(true, true)
            }
        }
    }
})