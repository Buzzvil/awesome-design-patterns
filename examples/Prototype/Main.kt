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
    /*
    만약 Robot.clone()에서 head와 body를 copy()하지 않는다면
    앝은 복사가 되어 다음과 같이 robot과 clone이 동시에 변경됨
    Robot@1e643faf: Head(eyes=new eyes, nose=my nose, lips=my lips)
    Robot@6e8dacdf: Head(eyes=new eyes, nose=my nose, lips=my lips)
    */
}

data class Head(var eyes: String, var nose: String, var lips: String)
data class Body(var arms: String, var legs: String)

// Java의 최상위 개체인 Object에는 Cloneable이 protected로 정의되어 있기 때문에
// 직접 만든 클래스에서 clone()을 "오버라이드" 하려면 Cloneable을 implement 해야 한다.
// (그냥 자체적으로 clone() 메서드를 구현해도 되지만, 일반적으로는 오버라이드 해서 구현하는 편)
class Robot(val head: Head, val body: Body) : Cloneable {
    public override fun clone(): Robot {
        // Kotlin의 data class에서 제공하는 copy() 메서드를 활용함
        return Robot(head.copy(), body.copy())

        // 얕은 복사
        // return Robot(head, body)

        // super.clone()으로 간단하게 복사할 수 있으나 이것도 얕은 복사(모든 멤버 변수가 primary라면 괜찮을듯)
        // return super.clone() as Robot
    }
}
