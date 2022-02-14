import org.scalatest.flatspec.AnyFlatSpec

import scala.reflect.runtime.universe.typeOf

class StudentListSpec extends AnyFlatSpec {

  "size method" should "return the size of StudentList collection" in {
    val emptyStudentList = new StudentList()
    assert (emptyStudentList.size == 0)
  }

  "append method" should "append student object to StudentList collection" in {
    val studentList = new StudentList()
    studentList.append(Student("Tom", 20))

    assert(studentList.size == 1)
  }

  "iterator method" should "return iterator of IterableStudentList" in {
    val iterableStudentList = new IterableStudentList()
    iterableStudentList append Student("A", 11)
    iterableStudentList append Student("C", 13)
    iterableStudentList append Student("B", 12)

    val studentListIterator = iterableStudentList.iterator

    assert(studentListIterator.next().age == 11)
    assert(studentListIterator.next().name == "C")
    assert(studentListIterator.hasNext == true)
  }
}
