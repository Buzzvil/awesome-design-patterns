package model

class Sandwich {
    private var bread: Bread = Bread.White
    private val meats: ArrayList<Meat> = ArrayList()
    private val cheeses: ArrayList<Cheese> = ArrayList()
    private val sauces: ArrayList<Sauce> = ArrayList()
    private val vegetables: ArrayList<Vegetable> = ArrayList()

    fun chooseBread(bread: Bread) {
        this.bread = bread
    }

    fun addMeat(meat: Meat) {
        meats.add(meat)
    }

    fun addCheese(cheese: Cheese) {
        cheeses.add(cheese)
    }

    fun addSauce(sauce: Sauce) {
        sauces.add(sauce)
    }

    fun addVegetable(vegetable: Vegetable) {
        vegetables.add(vegetable)
    }

    override fun toString(): String {
        return "$meats 샌드위치"
    }
}
