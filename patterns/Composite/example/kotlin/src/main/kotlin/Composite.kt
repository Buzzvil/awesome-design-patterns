class Composite: Component {
    var children: MutableList<Component> = mutableListOf<Component>()

    fun add(component: Component) {
        this.children.add(component)
    }

    fun getChildren(): List<Component> {
        return this.children
    }

    override fun execute(): Int {
        return 3
    }
}