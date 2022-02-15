import io.kotest.core.spec.style.BehaviorSpec
import kotlin.test.assertEquals

class CartIteratorTests: BehaviorSpec({
    given("2개의 상품이 들어있는 Cart 객체가 있다.") {
        val cart = Cart(listOf(Product("water", 1000), Product("cola", 1000)))

        and ("Cart 객체를 iterating 하는 CartIterator 객체가 있다."){
            val cartIterator = CartIterator(cart)

            `when` ("hasNext 를 호출한다") {
                val actualHasNext = cartIterator.hasNext()

                then("cartIterator 의 hasNext 는 true를 반환해야 한다.") {
                    assertEquals(true, actualHasNext)
                }
            }

            `when` ("next 를 2번 호출한다") {
                val actualNext1 = cartIterator.next()
                val actualNext2 = cartIterator.next()

                then("첫번째는 'water'인 상품, 두번째는 'cola' 인 상품을 반환해야 한다.") {
                    assertEquals("water", actualNext1?.name)
                    assertEquals("cola", actualNext2?.name)
                }

                and ("next 모두 호출 후 hasNext 를 호출한다") {
                    val actualHasNext = cartIterator.hasNext()

                    then("Iterating 이 끝났기 때문에 false 를 반환해야 한다.") {
                        assertEquals(false, actualHasNext)
                    }
                }
            }
        }
    }
})