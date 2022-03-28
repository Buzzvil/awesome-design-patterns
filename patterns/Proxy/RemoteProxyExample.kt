// 원격(remote) 프록시: 원격 서비스의 로컬 실행
interface Company {
    fun requestVoiceOfCustomer(): String
}

class HeadOffice : Company {
    override fun requestVoiceOfCustomer(): String {
        return "Thank you."
    }
}

class BranchOffice(private val headOffice: HeadOffice) : Company {
    override fun requestVoiceOfCustomer(): String {
        // 고객은 본사로 직접 문의하지 않고도 지사를 통해 문의할 수 있음
        // 번역 작업(마샬링)을 지사(프록시)에서 수행
        return translate(headOffice.requestVoiceOfCustomer())
    }

    private fun translate(string: String): String {
        return "감사합니다."
    }
}
