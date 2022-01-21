class Node[T](value: T, left: Option[Node[T]] = null, right: Option[Node[T]] = null)

class BinaryTree [T]() {
  val root: Option[T] = null

  def add(v: T): T = {
    this.leafNode()
  }

  def leafNode(): Node[T] = findEmptyNode(this.root)

  def findEmptyNode(node: Node[T]): Node[T]
}
