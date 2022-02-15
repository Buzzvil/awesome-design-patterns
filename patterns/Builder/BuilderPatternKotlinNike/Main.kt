import model.Bread
import model.Cheese
import model.Sauce
import model.Vegetable

fun main(args: Array<String>) {
    val staff = SubwayStaff()
    staff.sayHello()

    val bmtSandwich = staff.makeSandwich(
        BmtSandwichBuilder(),
        bread = Bread.ParmesanOregano,
        cheeses = arrayOf(
            Cheese.American
        ),
        sauces = arrayOf(
            Sauce.OliveOil,
            Sauce.RedWineVinaigrette
        ),
        vegetables = arrayOf(
            Vegetable.Lettuce,
            Vegetable.Tomatoes,
            Vegetable.RedOnions,
            Vegetable.Peppers,
            Vegetable.Olives,
            Vegetable.Pickles
        )
    )
    staff.serveSandwich(bmtSandwich)

    val eggMayoSandwich = staff.makeSandwich(
        EggMayoSandwichBuilder(),
        bread = Bread.White,
        cheeses = arrayOf(
            Cheese.American
        ),
        sauces = arrayOf(
            Sauce.Mayonnaise,
            Sauce.HoneyMustard
        ),
        vegetables = arrayOf(
            Vegetable.Cucumbers
        )
    )
    staff.serveSandwich(eggMayoSandwich)

    val mySandwich = staff.makeMyFavoriteSandwich()
    staff.serveSandwich(mySandwich)
}
