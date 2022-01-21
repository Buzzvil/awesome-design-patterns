import org.scalatest.FunSuite

class CustomIteratorTest extends FunSuite {
  test("How to make Iterator") {
    class MyIterator extends CustomIterator[Int] {
      override def hasNext(): Boolean = false
      override def next(): Int = 3
    }

    val myIterator = new MyIterator()
    assert(myIterator.hasNext() === false)
    assert(myIterator.next() === 3)
  }
}
