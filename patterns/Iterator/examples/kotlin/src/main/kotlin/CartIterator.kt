class CartIterator(cart: Cart): IteratorInterface<Product>{
    private val cart = cart
    private val index = 0
    override fun hasNext(): Boolean = index < cart.getSize()
    override fun next(): Product = Product("", 3)
}