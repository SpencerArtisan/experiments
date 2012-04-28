package skw

class Account(initialBalance: Double) {
  protected var balance = initialBalance
  
  def deposit(amount: Double) = {
      balance += amount; balance 
  } 
  
  def withdraw(amount: Double) = { 
      balance -= amount; balance 
  }
}

class CheckingAccount(initialBalance: Double) extends Account(initialBalance) {
  override def deposit(amount: Double) = { balance -= 1.0; super.deposit( amount)}
 
  def getBalance() = {
      balance
  }
}

abstract class Item {
  val price : Double
  val description : String
}

class SimpleItem(val price: Double, val description: String) extends Item {
}

