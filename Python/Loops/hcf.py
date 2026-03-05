a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
hcf = 1
for i in range(1,min(a,b)+1):
  if a%i==0 and b%i==0:
    hcf = i
print("HCF of",a,"and",b,"is",hcf)  