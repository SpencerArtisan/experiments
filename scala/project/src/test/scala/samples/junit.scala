package samples

import org.junit._
import Assert._
import skw._

@Test
class AppTest {
    @Test
    def testOK() = assertTrue(true)

    @Test
    def testBankAccount() = {

      var account = new BankAccount()
      println(account.balance())
      account.deposit(12.34)
      println(account.balance())
      account.withdraw(6.37)
      println(account.balance())
    }

    @Test
    def testTime() = {
      var early = new Time(9, 15)
      var late = new Time(23, 58)
      assertTrue(early.before(late))
      assertFalse(late.before(early))
      assertFalse(early.before(early))
    }

    @Test
    def testConversion() = {
      println(Conversions.milesToKilometers(5.0)) 
      assertEquals(8.0, Conversions.milesToKilometers(5.0), 0.0001)
    }

    @Test
    def testPoint() = {
      var p = Point2(3,5)
      assertEquals(3.0, p.x, 0.0001)
      assertEquals(5.0, p.y, 0.0001)
    } 

    @Test
    def testSuits() = {
      println(Suit.Spades)
      println(Suit.Clubs)
      println(Suit.Diamonds)
      println(Suit.Hearts)
    }

    @Test
    def testCheckingAccount() = {
      var account = new CheckingAccount(100.00)
      assertEquals(100.00, account.getBalance(), 0.001)  
      account.deposit(10.0)
      assertEquals(109.00, account.getBalance(), 0.001)
    } 

    @Test
    def testItem() = {
      var item : Item = null
      item = new SimpleItem(123.45, "coal")
      assertEquals(123.45, item.price, 0.001)
      assertEquals("coal", item.description)
    }

    @Test
    def testFileStuff() = {
      FileStuff.reverse("song.txt")
    }

    @Test
    def testTraits() = {
      var points = Array(new OrderedPoint(7,0), new OrderedPoint(12,2), new OrderedPoint(1,2))
      var sortedPoints = points.sorted.toArray
      for (p <- sortedPoints) println(p)
    }
}



