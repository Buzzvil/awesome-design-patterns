class Box: Component {
    private val children = mutableListOf<Component>()

    fun add(component: Component) {
        this.children.add(component)
    }

    fun remove(component: Component): Boolean = this.children.remove(component)

    override fun getTotalPrice(): Int = this
        .children.fold(0) { acc, next -> acc + next.getTotalPrice() }
}