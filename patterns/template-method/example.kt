fun main(args: Array<String>) {
    val originalRamen = OriginalRamen()
    originalRamen.build()
    /*
    물을 끓입니다.
    스프를 넣습니다.
    면을 넣습니다.
    파송송 계란탁
     */

    val hangoverRamen = HangoverRamen()
    hangoverRamen.build()
    /*
    물을 끓입니다.
    스프를 넣습니다.
    면을 넣습니다.
    김치를 넣습니다.
    콩나물을 넣습니다.
     */

    val spaghetti = Spaghetti()
    spaghetti.build()
    /*
    물을 면이 잠길 정도만 넣습니다.
    스프를 지금 넣지 않습니다.
    면을 넣습니다.
    스프를 넣고 잘 섞어줍니다.
     */
}

abstract class Ramen {
    fun build() {
        boilWater()
        addSoupPowder()
        addNoodle()
        addExtra()
    }

    protected open fun boilWater() {
        println("물을 끓입니다.")
    }

    protected open fun addSoupPowder() {
        println("스프를 넣습니다.")
    }

    protected open fun addNoodle() {
        println("면을 넣습니다.")
    }

    protected abstract fun addExtra()
}

class OriginalRamen : Ramen() {
    override fun addExtra() {
        println("파송송 계란탁")
    }
}

class HangoverRamen : Ramen() {
    override fun addExtra() {
        println("김치를 넣습니다.")
        println("콩나물을 넣습니다.")
    }
}

class Spaghetti : Ramen() {
    override fun boilWater() {
        println("물을 면이 잠길 정도만 넣습니다.")
    }

    override fun addSoupPowder() {
        println("스프를 지금 넣지 않습니다.")
    }

    override fun addExtra() {
        println("스프를 넣고 잘 섞어줍니다.")
    }
}
