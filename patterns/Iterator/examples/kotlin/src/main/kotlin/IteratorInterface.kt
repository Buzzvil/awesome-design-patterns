interface IteratorInterface<T> {
    fun hasNext(): Boolean
    fun next(): T?
}