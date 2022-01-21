import org.scalatest.FunSuite

class CustomIteratorTest extends FunSuite {
  test("Haha") {
    assert(new Example().hasNext() === true)
  }
}
