trait CustomIterator[T] {
  def hasNext(): Boolean
  def next(): Option[T]
}
