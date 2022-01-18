// Kotlin은 Java와 다르게 public, private을 쓰지 않고도 singleton을 만들 수 있다 !!
object Coin {
  private var coin: Int = 0

  fun getCoin():Int {
    return coin
  }

  fun addCoin() {
    coin += 10
  }

  fun deductCoin() {
    coin--
  }
}
