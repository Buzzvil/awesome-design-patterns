class Product(private val price: Int): Component {
    override fun getTotalPrice(): Int = this.price
}