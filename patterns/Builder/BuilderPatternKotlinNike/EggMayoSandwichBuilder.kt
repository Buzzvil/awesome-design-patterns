import model.Meat

class EggMayoSandwichBuilder : SandwichBuilder() {
    override fun buildMeat() {
        sandwich.addMeat(Meat.EggMayo)
    }
}
