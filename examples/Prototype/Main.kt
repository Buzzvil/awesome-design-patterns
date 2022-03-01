fun main(args: Array<String>) {
    val head = Head(eyes = "my eyes", nose = "my nose", lips = "my lips")
    val body = Body(arms = "my arms", legs = "my legs")
    val robot = Robot(head, body)
    val clone = robot.clone()

    println("$robot: ${robot.head}")
    println("$clone: ${clone.head}")
    /*
    Robot@1e643faf: Head(eyes=my eyes, nose=my nose, lips=my lips)
    Robot@6e8dacdf: Head(eyes=my eyes, nose=my nose, lips=my lips)
    */

    clone.head.eyes = "new eyes"

    println("$robot: ${robot.head}")
    println("$clone: ${clone.head}")
    /*
    Robot@1e643faf: Head(eyes=my eyes, nose=my nose, lips=my lips)
    Robot@6e8dacdf: Head(eyes=new eyes, nose=my nose, lips=my lips)
    */
}

data class Head(var eyes: String, var nose: String, var lips: String)
data class Body(var arms: String, var legs: String)

// Java의 최상위 개체인 Object에는 Cloneable이 protected로 정의되어 있기 때문에
// 직접 만든 클래스에서 clone()을 "오버라이드" 하려면 Cloneable을 implement 해야 한다.
// (그냥 자체적으로 clone() 메서드를 구현해도 되지만, Java/Kotlin을 사용할 때는 일반적으로 오버라이드 해서 구현하는 편)
class Robot(val head: Head, val body: Body) : Cloneable {
    public override fun clone(): Robot {
        // Kotlin의 data class에서 제공하는 copy() 메서드를 활용함
        return Robot(head.copy(), body.copy())
    }
}
