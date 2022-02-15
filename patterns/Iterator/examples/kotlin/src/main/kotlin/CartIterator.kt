class CartIterator: IteratorInterface<Product>{
    override fun hasNext(): Boolean = true
    override fun next(): Product = Product("", 3)
}