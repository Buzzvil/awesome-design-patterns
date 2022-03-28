
case class Student(name: String, age: Int)

trait StudentListTrait {
  var studentList = List.empty[Student]
  def append(student: Student): Unit
  def size: Int
}

class StudentList extends StudentListTrait {
  def append(student: Student): Unit = {
    studentList :+= student
  }

  override def size: Int = studentList.size
}

class IterableStudentList extends StudentList with Iterable[Student] {
  override def size: Int = studentList.size
  def iterator: Iterator[Student] = studentList.iterator
}