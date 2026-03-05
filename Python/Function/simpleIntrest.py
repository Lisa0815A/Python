def simpleIntrest(p,t,r):
  si = (p*t*r)/100
  return si
principal = float(input("Enter the principal amount:"))
time = float(input("Enter the time in year:"))
rate = float(input("Enter the rate of intrest:"))
result = simpleIntrest(principal,time,rate)
print("The simple intrestt is:",result)