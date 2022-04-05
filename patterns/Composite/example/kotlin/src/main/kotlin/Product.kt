class Product(private val price: Int): Component {
    override fun execute(): Int = this.price
}