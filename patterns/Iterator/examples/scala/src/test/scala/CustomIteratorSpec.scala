import org.scalatest.flatspec.AnyFlatSpec

class CustomIteratorSpec extends AnyFlatSpec {
  class MyIterator extends CustomIterator[Int] {
    override def hasNext(): Boolean = false
    override def next(): Int = 3
  }

  "A custom Iterator" should "have haxNext() and next()" in {

    val iterator = new MyIterator
    assert(iterator.hasNext() === false)
    assert(iterator.next() === 3)
  }

  it should ""
}

