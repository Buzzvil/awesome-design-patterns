import org.scalatest.flatspec.AnyFlatSpec

class IteratorProsSpec extends AnyFlatSpec {
  val exampleStudentList = new StudentList()
  exampleStudentList append Student("A", 11)
  exampleStudentList append Student("C", 13)
  exampleStudentList append Student("B", 12)

  it should "implement new types of iterators and pass them to existing code without breaking anything" in {
    def sumAges(iterator: Iterator[Student]): Int = iterator.foldLeft(0) (_+_.age)

    val iterator = exampleStudentList.iterator
    assert(sumAges(iterator) == 36)

    class ReversedStudentList() extends StudentList {
      override def iterator: Iterator[Student] = studentList.reverse.iterator
    }
    val myStudentList = new ReversedStudentList()
    myStudentList.studentList = exampleStudentList.studentList

    val newIterator = myStudentList.iterator
    assert(sumAges(newIterator) == 36)
  }

  "multiple iterators" should "iterate over the same collection in parallel" in {
    val iterator1 = exampleStudentList.iterator
    val iterator2 = exampleStudentList.iterator

    assert(iterator1.next().name == "A")
    assert(iterator2.next().name == "A")

    assert(iterator1.next().name == "C")
    assert(iterator2.next().name == "C")

    assert(iterator1.next().name == "B")
    assert(iterator2.next().name == "B")
  }

  "Iterator" should "work when delayed" in {
    val iterator1 = exampleStudentList.iterator
    assert(iterator1.next().age == 11)

    val iterator2 = exampleStudentList.iterator
    assert(iterator2.hasNext)

    assert(iterator1.next().age == 13)
  }
}
