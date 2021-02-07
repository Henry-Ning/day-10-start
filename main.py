def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  """
  Docstring. interpreted as comment

  """
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2:
    return 29
  return month_days[month - 1]   
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# What you knowThese are questions you got right on the first try.
# Without running the code below, what do you think will be printed in the console? def add(n1, n2): return n1 + n2 def subtract(n1, n2): return n1 - n2 def multiply(n1, n2): return n1 * n2 def divide(n1, n2): return n1 / n2 print(add(2, multiply(5, divide(8, 4))))
# What would you predict to be the result of running the following code?def outer_function(a, b): def inner_function(c, d): return c + d return inner_function(a, b) result = outer_function(5, 10) print(result)
# What will be printed in the console after running the following code?def my_function(a): if a < 40: return print("Terrible"










