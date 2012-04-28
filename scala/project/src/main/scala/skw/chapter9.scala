package skw
import scala.io.Source

object FileStuff {
    def reverse(filename : String) = {
        var lines = Source.fromFile(filename).getLines.toArray.reverse
        for (line <- lines) println(line)
        }
}
