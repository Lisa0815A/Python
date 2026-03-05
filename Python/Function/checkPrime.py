def checkPrime():
  num = int(input("Enter a number:"))
  if num > 1:
    for i in range(2,num):
      if (num%i) == 0:
        print(num,"Is not a prime number")
        break
      else:
        print(num,"is a prime number")

checkPrime()        