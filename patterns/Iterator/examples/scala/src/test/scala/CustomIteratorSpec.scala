import org.scalatest.flatspec.AnyFlatSpec

class CustomIteratorSpec extends AnyFlatSpec {
  "A custom Iterator" should "have haxNext() and next()" in {
    class MyIterator extends CustomIterator[Int] {
      override def hasNext(): Boolean = false
      override def next(): Int = 3
    }
    val iterator = new MyIterator
    assert(iterator.hasNext() === false)
    assert(iterator.next() === 3)
  }
}

