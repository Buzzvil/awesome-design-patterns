import model.Bread
import model.Cheese
import model.Meat
import model.Sandwich
import model.Sauce
import model.Vegetable

class SandwichFluentBuilder {
    private var sandwich: Sandwich = Sandwich()

    fun createNewSandwich(): SandwichFluentBuilder {
        sandwich = Sandwich()
        return this
    }

    fun chooseBread(bread: Bread): SandwichFluentBuilder {
        sandwich.chooseBread(bread)
        return this
    }

    fun addMeat(meat: Meat): SandwichFluentBuilder {
        sandwich.addMeat(meat)
        return this
    }

    fun addCheese(cheese: Cheese): SandwichFluentBuilder {
        sandwich.addCheese(cheese)
        return this
    }

    fun addSauce(sauce: Sauce): SandwichFluentBuilder {
        sandwich.addSauce(sauce)
        return this
    }

    fun addVegetable(vegetable: Vegetable): SandwichFluentBuilder {
        sandwich.addVegetable(vegetable)
        return this
    }

    fun build(): Sandwich {
        return sandwich
    }
}
