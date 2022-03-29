class Cart(products: List<Product>) {
    private val cartProducts = products
    fun getSize(): Int = cartProducts.size
    fun getProducts(): List<Product> = cartProducts
}