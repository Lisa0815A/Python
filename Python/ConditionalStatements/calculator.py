a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
operator = input("Enter operator(+,-,*,/):")
if operator == '+':
  print("Result:",a+b)
elif operator == '-':
  print("Result:",a-b)
elif operator == '*':
  print("Result:",a*b)
elif operator == '/':
  if b!= 0:
    print("Result:",a/b)
  else:
    print("Error: Division by zero")
else:
  print("Invalid operator")