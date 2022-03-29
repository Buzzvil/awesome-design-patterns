class CartIterator(cart: Cart): IteratorInterface<Product>{
    private val cart = cart
    private var index = 0
    override fun hasNext(): Boolean = index < cart.getSize()
    override fun next(): Product? {
        index += 1
        return cart.getProducts().elementAtOrNull(index - 1)
    }
}