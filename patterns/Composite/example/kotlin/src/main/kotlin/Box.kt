class Box(override val name: String): Component {
    val children = mutableListOf<Box>()

    fun add(composite: Box) {
        this.children.add(composite)
    }

    override fun isLeaf() = this.children.isEmpty()

    override fun execute(): Int = this.children.fold(0) { acc, next -> acc + next.execute() }
}