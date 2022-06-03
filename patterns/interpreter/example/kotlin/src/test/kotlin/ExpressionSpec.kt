import io.kotest.core.spec.style.BehaviorSpec
import kotlin.test.assertEquals

class TerminalExpressionSpec: BehaviorSpec({
    given("banana 라는 context 를 가진 TerminalExpression 이 있다.") {
        val bananaTerminalExpression = TerminalExpression("banana")

        `when` ("context 와 동일한 data 로 interpreter 를 수행한다"){
            val result = bananaTerminalExpression.interpreter("banana")

            then("interpreter 는 context 와 data가 같은 경우 true 를 반환해야 한다") {
                assertEquals(true, result)
            }
        }

        `when` ("context 와 다른 data 로 interpreter 를 수행한다.") {
            val result = bananaTerminalExpression.interpreter("apple")

            then("interpreter 는 context 와 data가 다른 경우 false 를 반환해야 한다") {
                assertEquals(false, result)
            }
        }
    }

})

class OrExpressionSpec: BehaviorSpec({
    given("2개의 TerminalExpression 이 주어진다. 해당 expression 들을 이용해 OrExpression 이 주어진다.") {
        val fruit1 = TerminalExpression("apple")
        val fruit2 = TerminalExpression("banana")
        val orExpression = OrExpression(fruit1, fruit2)

        `when` ("orExpression 이 포함한 data 로 interpreter 를 수행한다.") {
            val result = orExpression.interpreter("banana")

            then("data 가 orExpression 에 포함됐다면 true 를 return 해야 한다.") {
                assertEquals(true, result)
            }
        }

        `when` ("orExpression 이 포함하지 않은 data 로 interpreter 를 수행한다.") {
            val result = orExpression.interpreter("kiwi")

            then("data 가 orExpression 에 포함되지 않았다면 false 를 return 해야 한다.") {
                assertEquals(false, result)
            }
        }
    }

})


class ExpressionSpec: BehaviorSpec({
    given("2개의 과일 expression 과 이를 포함한 OrExpression 을 통해 isSingle 이라는 interpreter 를 생성한다.") {
        val fruit1 = TerminalExpression("apple")
        val fruit2 = TerminalExpression("banana")
        val isSingle = OrExpression(fruit1, fruit2)

        `when` ("isSingle 을 통해 존재하는 과일로 interpreter 를 수행한다.") {
            val result = isSingle.interpreter("banana")

            then("존재하는 과일은 true 를 return해야 한다.") {
                assertEquals(true, result)
            }
        }

        `when` ("isSingle 을 통해 존재하지 않는 과일로 interpreter 를 수행한다.") {
            val result = isSingle.interpreter("kiwi")

            then("존재하지 않는 과일은 false 를 return해야 한다.") {
                assertEquals(false, result)
            }
        }
    }
})