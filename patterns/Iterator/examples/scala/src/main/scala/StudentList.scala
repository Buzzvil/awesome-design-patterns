
case class Student(name: String, age: Int)

class StudentList {
  var studentList = List.empty[Student]

  def append(student: Student): Unit ={
    studentList = studentList :+ student
  }

  def size: Int = studentList.size

  def iterator: Iterator[Student] = studentList.iterator
}
