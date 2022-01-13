import model.Bread
import model.Cheese
import model.Meat
import model.Sandwich
import model.Sauce
import model.Vegetable

class SubwayStaff {
    fun sayHello() {
        println("어서오세요~ 서브웨이입니다~")
    }

    fun makeSandwich(
        sandwichBuilder: SandwichBuilder,
        bread: Bread,
        cheeses: Array<Cheese>,
        sauces: Array<Sauce>,
        vegetables: Array<Vegetable>
    ): Sandwich {
        sandwichBuilder.createNewSandwich()
        sandwichBuilder.buildBread(bread)
        sandwichBuilder.buildMeat()
        sandwichBuilder.buildCheese(*cheeses)
        sandwichBuilder.buildSauce(*sauces)
        sandwichBuilder.buildVegetable(*vegetables)

        return sandwichBuilder.sandwich
    }

    fun makeMyFavoriteSandwich(): Sandwich {
        val sandwichFluentBuilder = SandwichFluentBuilder()
            .createNewSandwich()
            .chooseBread(Bread.ParmesanOregano)
            .addMeat(Meat.Turkey)
            .addCheese(Cheese.Shredded)
            .addSauce(Sauce.Ranch)
            .addSauce(Sauce.SmokeBBQ)

        for (vegetable in Vegetable.values()) {
            sandwichFluentBuilder.addVegetable(vegetable)
        }

        return sandwichFluentBuilder.build()
    }

    fun serveSandwich(sandwich: Sandwich) {
        println("주문하신 $sandwich 나왔습니다~")
    }
}
