from art import logo
#Add
def add (n1,n2):
  return n1 + n2
  
#Subtract
def subtract (n1,n2):
  return n1 - n2

#Multiply
def multiply (n1,n2):
  return n1 * n2

#Divide
def divide (n1,n2):
  return n1 / n2



#Operations dictionary
operations = {
"+":add,
"-":subtract,
"*":multiply,
"/":divide
}

#Continuation
from replit import clear
def coun(num1,next_num,l):
  another_calc = operations[l]
  return another_calc(num1,next_num)
def calculator():
  print(logo)
  num1 = float(input("What's the first number?:"))
  
  
  for symbol in operations:
    print (symbol)
  
  choice = "y"
  while choice == "y":
    l = input("Pick an operation: ")
    next_num = float(input("What's the next number?: "))
    j = coun(num1,next_num,l)
    print(f"{num1} {l} {next_num} = {j}")
    num1 = j
    choice = input(f"Type 'y' to continue calculating with {num1}, or type 'n' to exit: ")
  
  if choice == "n":
    clear()
    calculator()

calculator()