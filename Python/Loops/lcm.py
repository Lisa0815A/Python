a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
max_num = max(a,b)
while True:
  if max_num % a==0 and max_num % b==0:
    print("LCM of",a,"and",b,"is",max_num)
    break
  max_num +=1