import io.kotest.core.spec.style.BehaviorSpec
import kotlin.test.assertEquals

class CartIteratorTests: BehaviorSpec({
    given("2개의 상품이 들어있는 Cart 객체가 있다.") {
        val cart = Cart(listOf(Product("water", 1000), Product("cola", 1000)))

        and ("Cart 객체를 iterating 하는 CartIterator 객체가 있다."){
            val cartIterator = CartIterator(cart)

            `when` ("hasNext 를 호출한다") {
                val actualHasNext = cartIterator.hasNext()

                then("cartIterator 의 hasNext 는 참을 반환해야 한다.") {
                    assertEquals(true, actualHasNext)
                }
            }

            `when` ("next 를 호출한다") {
                val actualNext = cartIterator.next()

                then("cartIterator 의 next 는 이름이 'water'인 상품을 반환해야 한다.") {
                    assertEquals("water", actualNext?.name)
                }
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