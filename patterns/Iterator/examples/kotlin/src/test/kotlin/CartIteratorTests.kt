import io.kotest.core.spec.style.BehaviorSpec
import kotlin.test.assertEquals

class CartIteratorTests: BehaviorSpec({
    given("2개의 상품이 들어있는 카트가 있다.") {
        val cart = Cart(listOf(Product("water", 1000), Product("cola", 1000)))

        `when` ("CartIterator 를 생성한다.") {
            val cartIterator = CartIterator(cart)

            then("iterator 의 hasNext 는 참을 반환해야 한다.") {
                assertEquals(true, cartIterator.hasNext())
            }
        }

//        `when` ("Cart 객체에 담긴 상품 리스트를 요청했다.") {
//            val actualList = emptyCart.getProducts()
//
//            then("빈 리스트가 반환되어야 한다.") {
//                assertEquals(actualList, listOf())
//            }
//        }
    }
})