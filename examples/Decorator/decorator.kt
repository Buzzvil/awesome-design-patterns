abstract class PizzaDecorator (private val pizza: Pizza) : Pizza {
  override fun decorate(): String {
    return pizza.decorate()
  }
}

class Pepperoni(pizza: Pizza) : PizzaDecorator(pizza) {
  override fun decorate() : String {
    return super.decorate() + decorateWithPepperoni()
  }

  private fun decorateWithPepperoni(): String {
    return " with Pepperoni"
  }
}

class Olive(pizza: Pizza) : PizzaDecorator(pizza) {
  override fun decorate() : String {
    return super.decorate() + decorateWithOlive()
  }

  private fun decorateWithOlive(): String {
    return " with Olive"
  }
}