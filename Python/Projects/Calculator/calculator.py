def calculator():
  a= int(input("Enter first number :"))
  b = int(input("Enter second number :"))
  print("Select operation : +, -, *, %, **, ***, //")
  operation = input("Enter operation")
  if operation == "+":
    print("Addition :",a+b)
  elif operation == "-":
    print("Substraction :",a-b)
  elif operation == "*":
    print("Multiplication :",a*b)
  elif operation == "%":
    print("Division :",a/b)
  elif operation == "**":
    print("square num:",a**b)
  elif operation == "***":
    print("cube num:",a**b)  
  elif operation == "//":    
    print("floor division :",a//b)
  else:
    print("Invalid operation")

calculator()              