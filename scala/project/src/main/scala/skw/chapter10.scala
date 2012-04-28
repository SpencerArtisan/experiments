package skw
import java.awt.Point
import scala.math.Ordered

class OrderedPoint(x: Int, y : Int) extends Point(x,y) with Ordered[OrderedPoint] {
  def compare(other : OrderedPoint) = x - other.x
  override def toString  = x.toString + " : " + y.toString
}

// vim: set ts=4 sw=4 et:
