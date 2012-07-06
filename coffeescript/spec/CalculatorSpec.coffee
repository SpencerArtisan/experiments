describe "Calculator", ->
  calculator = null

  beforeEach ->
    calculator = new Calculator

  it "can add two positive numbers", ->
    result = calculator.add 2, 3
    (expect result).toBe 5

  it "can subtract a negative from a positive", ->
    result = calculator.subtract 4, -6
    (expect result).toBe 10


