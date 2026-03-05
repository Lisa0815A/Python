def fibonacci(n):
    if n <= 1:          # base case
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)   # recursive call


num = int(input("Enter number of terms: "))

for i in range(num):
    print(fibonacci(i), end=" ")