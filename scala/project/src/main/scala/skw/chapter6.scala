package skw

object Conversions {
    def milesToKilometers(miles: Double) = {miles * 8.0 / 5.0}
}

class Point2(var x: Double, var y: Double) {
}

object Point2 {
    def apply(x: Double, y: Double) = new Point2(x,y)
}

object Suit extends Enumeration {
  val Clubs = Value("clb")
  val Hearts = Value("♥")
  val Spades = Value("♠")
  val Diamonds = Value("\u0041")
}
