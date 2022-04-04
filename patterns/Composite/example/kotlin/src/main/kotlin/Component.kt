interface Component {
    val name: String
    fun isLeaf(): Boolean
    fun execute(): Int
}