import org.scalatest.flatspec.AnyFlatSpec

class CreatorSpec extends AnyFlatSpec {
  "Create interface" should "not know about ConcreteProduct" in {
    class PepsiProduct extends Product {
      override def name: String = "pepsi"
      override def price: Float = 300
    }

    object PepsiCreator extends Creator {
      override def FactoryMethod(): Product = new PepsiProduct()
    }

    assert(PepsiCreator.FactoryMethod().name == "pepsi")
  }
}
