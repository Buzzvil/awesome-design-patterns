import org.scalatest.flatspec.AnyFlatSpec

class CandyCreatorSpec extends AnyFlatSpec {
  "Factory method" should "return candy instance" in {
    val candy = CandyCreator.FactoryMethod()
    assert(candy.price == 500)
    assert(candy.name == "candy")
  }


}
