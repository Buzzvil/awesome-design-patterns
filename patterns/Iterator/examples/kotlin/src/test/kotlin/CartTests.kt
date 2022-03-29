import io.kotest.core.spec.style.BehaviorSpec
import kotlin.test.assertEquals

class CartTests: BehaviorSpec({
    given("2개의 상품이 들어있는 Cart 객체가 있다.") {
        val cart = Cart(listOf(Product("water", 1000), Product("cola", 1000)))

        `when` ("Cart 객체에 담긴 상품 수를 요청했다.") {
            val actualSize = cart.getSize()

            then("상품 수는 2이어야 한다.") {
                assertEquals(2, actualSize)
            }
        }

        `when` ("Cart 객체에 담긴 상품 리스트를 요청했다.") {
            val actualList = cart.getProducts()

            then("리스트의 첫번째 상품 이름은 'water' 이어야 한다.") {
                assertEquals("water", actualList[0].name)
            }
        }
    }
})