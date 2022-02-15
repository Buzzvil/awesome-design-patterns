// Kotlin은 Java와 다르게 public, private을 쓰지 않고도 singleton을 만들 수 있다.
object Coin {
  var coin: Int = 0
    private set

  fun addCoin() {
    coin += 10
  }

  fun deductCoin() {
    coin--
  }
}
