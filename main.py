def add(n1, n2):
  return n1+n2

def subtract(n1, n2):
  return n1-n2

def multiply(n1, n2):
  return n1*n2

def divide(n1, n2):
  return n1/n2


operations = {"+": add, "-": subtract, "*": multiply, "/":divide}

num1 = int(input("first number: "))
num2 = int(input("second number: "))

for symbol in operations:
  print(symbol)

operation_symbol = input("opearation: ")

calculation_function = operations[operation_symbol]
print(calculation_function(num1, num2))

