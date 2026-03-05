a = int(input("enter the number :"))
reverse =0
while a>0:
  reminder = a%10
  reverse = (reverse*10)+reminder
  a = a//10
print("the reverse is :",reverse)  