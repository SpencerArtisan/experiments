package skw

class BankAccount {
    private var bal = 0.0
    def deposit(amount:Double) { bal += amount }
    def withdraw(amount:Double) { bal -= amount }
    def balance():Double = bal
}

class Time(var hours: Int, var mins: Int) {
  def before(other:Time) = { hours < other.hours }
}
