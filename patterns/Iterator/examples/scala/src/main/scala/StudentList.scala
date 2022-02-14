
case class Student(name: String, age: Int)

trait StudentListTrait {
  var studentList = List.empty[Student]
  def append(student: Student): Unit
  def size: Int
  def iterator: Iterator[Student]
}

class StudentList extends StudentListTrait {
  def append(student: Student): Unit ={
    studentList = studentList :+ student
  }

  def size: Int = studentList.size

  def iterator: Iterator[Student] = studentList.iterator
}
