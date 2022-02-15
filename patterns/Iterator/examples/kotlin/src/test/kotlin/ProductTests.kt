import io.kotest.core.spec.style.BehaviorSpec
import kotlin.test.assertEquals

class ProductTests: BehaviorSpec({
    given("이름은 'water'이고 가격은 1000원인 Product 객체가 있다.") {
        val product = Product("water", 1000)
        `when`("상품의 이름을 요청했다.") {
            then("반환된 이름은 'water' 이어야 한다.") {
                assertEquals("water", product.name)
            }
        }

        `when`("상품의 가격 요청했다.") {
            then("반환된 가격은 1000원 이어야 한다.") {
                assertEquals(1000, product.price)
            }
        }
    }

})
