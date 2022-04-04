class Composite: Component {
    val children: MutableList<Composite> = mutableListOf<Composite>()

    fun add(composite: Composite) {
        this.children.add(composite)
    }

    override fun isLeaf(): Boolean {
        return false
    }

    override fun execute(): Int {
        return 3
    }
}