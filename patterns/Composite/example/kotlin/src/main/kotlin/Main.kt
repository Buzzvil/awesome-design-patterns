fun main(args: Array<String>) {
    // Depth 3
    val phone = Product(price=500)
    val headphones = Product(price=400)
    val charger = Product(price=300)

    // Depth 2
    val hammer = Product(price=200)
    val phoneAndHeadphonesBox = Box()
    phoneAndHeadphonesBox.add(phone)
    phoneAndHeadphonesBox.add(headphones)
    val chargerBox = Box()
    chargerBox.add(charger)

    // Depth 1
    val hammerBox = Box()
    hammerBox.add(hammer)
    val boxOfBox = Box()
    boxOfBox.add(phoneAndHeadphonesBox)
    boxOfBox.add(chargerBox)
    val receipt = Product(price=100)

    // Depth 0
    val rootBox = Box()
    rootBox.add(hammerBox)
    rootBox.add(boxOfBox)
    rootBox.add(receipt)

    // all products price: 100 + 200 + 300 + 400 + 500 = 1500
    println(rootBox.getTotalPrice())

    // phone price: 500, headphones price: 400
    // phoneAndHeadphonesBox price: 500 + 400 = 900
    println(phone.getTotalPrice())
    println(headphones.getTotalPrice())
    println(phoneAndHeadphonesBox.getTotalPrice())
}