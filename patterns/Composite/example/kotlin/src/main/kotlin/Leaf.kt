class Leaf: Component {
    override fun isLeaf(): Boolean = true

    override fun execute(): Int {
        return 3
    }
}