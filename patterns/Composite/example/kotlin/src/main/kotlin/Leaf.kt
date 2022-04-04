class Leaf(override val name: String, private val price: Int): Component {
    override fun isLeaf(): Boolean = true

    override fun execute(): Int = this.price
}