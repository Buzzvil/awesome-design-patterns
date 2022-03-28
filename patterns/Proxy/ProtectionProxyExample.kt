// 보호(protection) 프록시: 엑세스 제어
interface NuclearBomb {
    fun launch()
}

class RealNuclearBomb : NuclearBomb {
    override fun launch() {
        println("The end.")
    }
}

class ProxyNuclearBomb(private val authorizedPerson: Person) : NuclearBomb {
    private val nuclearBomb = RealNuclearBomb()

    override fun launch() {
        // 인증 절차 추가
        if (authorizedPerson.name == "Mr. Kim") {
            nuclearBomb.launch()
        } else {
            println("The world is at peace.")
        }
    }
}
