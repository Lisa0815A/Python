a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))
if a>b and a>c:
  print("largest number is :",a)
elif b>c:
  print("largest number is :",b)
else:
  print("largest number is :",c)