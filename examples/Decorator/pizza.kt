interface Pizza {
  fun decorate(): String
}

class ThinPizza : Pizza {
  override fun decorate() = "Thin pizza"
}

fun pizzaWithPepperoni() {
  val thinPizza = Pepperoni(ThinPizza())
  val decoratedThinPizza = thinPizza.decorate()
  println(decoratedThinPizza)
}
