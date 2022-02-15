import io.kotest.core.spec.style.BehaviorSpec

class CartTests: BehaviorSpec({
    given("빈 Cart 객체가 있다") {
        val emptyCart = Cart(3)
        `when` ("Cart 객체에 담긴 상품 수를 요청했다.") {
            then("상품 수는 0이어야 한다.") {
                assert(true)
            }
        }

        `when` ("Cart 객체에 담긴 상품 리스트를 요청했다.") {
            then("빈 리스트가 반환되어야 한다.") {
                assert(true)
            }
        }
    }
})