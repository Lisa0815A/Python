a = int(input("enter the number:"))
original = a
count = len(str(a))
sum = 0
while a>0:
  digit = a%10  
  sum = sum + (digit**count)
  a = a//10
if sum == original:
  print("the number is armstrong.")
else:
  print("the number is not armstrong.")  
