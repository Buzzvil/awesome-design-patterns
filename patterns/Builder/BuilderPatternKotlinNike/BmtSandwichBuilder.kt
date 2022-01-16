import model.Meat

class BmtSandwichBuilder : SandwichBuilder() {
    override fun buildMeat() {
        sandwich.addMeat(Meat.Pepperoni)
        sandwich.addMeat(Meat.Salami)
        sandwich.addMeat(Meat.Ham)
    }
}
