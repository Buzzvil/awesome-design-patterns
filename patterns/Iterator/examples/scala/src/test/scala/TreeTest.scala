import org.scalatest.FunSuite

class TreeTest extends FunSuite {
  test("test initializeSampleTree") {
    val tree = Tree.initializedSampleTree()
    assert(tree.value === 3)
  }

}
