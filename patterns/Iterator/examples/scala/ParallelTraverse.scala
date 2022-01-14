// Parallel traverse

val list = List(3, 1, 2)
val iterator1 = list.iterator
val iterator2 = list.iterator

println(iterator1.next)
println(iterator1.next)
println(iterator2.next)
println(iterator2.next)
println(iterator2.next)
println(iterator1.next)
