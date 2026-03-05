num = int(input("enter the number:"))
sum = 0
while num>0:
  reminder = num%10
  sum = sum +reminder
  num = num//10
print("the sum of digit is:",sum)
  
