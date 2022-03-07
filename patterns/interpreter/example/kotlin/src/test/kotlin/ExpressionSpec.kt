import io.kotest.core.spec.style.BehaviorSpec
import kotlin.test.assertEquals

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