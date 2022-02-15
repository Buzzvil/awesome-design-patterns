import io.kotest.core.spec.style.BehaviorSpec
import kotlin.test.assertEquals

class CartTests: BehaviorSpec({
    given("빈 Cart 객체가 있다") {
        val emptyCart = Cart(listOf())

        `when` ("Cart 객체에 담긴 상품 수를 요청했다.") {
            val actualSize = emptyCart.getSize()

            then("상품 수는 0이어야 한다.") {
                assertEquals(0, actualSize)
            }
        }

        `when` ("Cart 객체에 담긴 상품 리스트를 요청했다.") {
            val actualList = emptyCart.getProducts()

            then("빈 리스트가 반환되어야 한다.") {
                assertEquals(actualList, listOf())
            }
        }
    }
})