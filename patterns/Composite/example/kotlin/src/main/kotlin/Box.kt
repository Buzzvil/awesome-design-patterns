class Box: Component {
    private val children = mutableListOf<Component>()

    fun add(component: Component) {
        this.children.add(component)
    }

    override fun getTotalPrice(): Int = this.children.fold(0) { acc, next -> acc + next.getTotalPrice() }
}