import org.scalatest.flatspec.AnyFlatSpec

class CustomIteratorSpec extends AnyFlatSpec {
  class MyIterator extends CustomIterator[Int] {
    override def hasNext(): Boolean = false
    override def next(): Option[Int] = Some(3)
  }

  "A custom Iterator" should "have haxNext() and next()" in {
    val iterator = new MyIterator
    assert(iterator.hasNext() === false)
    assert(iterator.next() === Some(3))
  }
}