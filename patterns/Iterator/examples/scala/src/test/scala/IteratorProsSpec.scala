import org.scalatest.flatspec.AnyFlatSpec

class IteratorProsSpec extends AnyFlatSpec {
  val exampleStudentList = new StudentList()
  exampleStudentList append Student("A", 11)
  exampleStudentList append Student("C", 13)
  exampleStudentList append Student("B", 12)

  "multiple iterators" should "iterate over the same collection in parallel" in {
    val iterator1 = exampleStudentList.iterator
    val iterator2 = exampleStudentList.iterator

    assert(iterator1.next().name == "A")
    assert(iterator1.next().name == "C")

    assert(iterator2.next().name == "A")

    assert(iterator1.next().name == "B")

    assert(iterator2.next().name == "C")
    assert(iterator2.next().name == "B")
  }
}
