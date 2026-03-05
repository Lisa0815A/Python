'''def pallindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        return True
    else:
        return False


number = int(input("Enter a number: "))

if pallindrome(number):
    print(number, "is a palindrome number.")
else:
    print(number, "is not a palindrome number.")'''

def palindrome(value):
    value = str(value)        # convert input to string
    if value == value[::-1]:  # reverse the string
        return True
    else:
        return False


data = input("Enter a number or string: ")

if palindrome(data):
    print(data, "is a palindrome.")
else:
    print(data, "is not a palindrome.")