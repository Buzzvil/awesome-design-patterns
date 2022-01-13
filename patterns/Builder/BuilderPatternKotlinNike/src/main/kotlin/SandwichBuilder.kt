import model.Bread
import model.Cheese
import model.Sandwich
import model.Sauce
import model.Vegetable

abstract class SandwichBuilder {
    var sandwich = Sandwich()
        private set

    abstract fun buildMeat()

    fun createNewSandwich() {
        sandwich = Sandwich()
    }

    fun buildBread(bread: Bread) {
        sandwich.chooseBread(bread)
    }

    fun buildCheese(vararg cheeses: Cheese) {
        for (cheese in cheeses) {
            sandwich.addCheese(cheese)
        }
    }

    fun buildSauce(vararg sauces: Sauce) {
        for (sauce in sauces) {
            sandwich.addSauce(sauce)
        }
    }

    fun buildVegetable(vararg vegetables: Vegetable) {
        for (vegetable in vegetables) {
            sandwich.addVegetable(vegetable)
        }
    }
}
