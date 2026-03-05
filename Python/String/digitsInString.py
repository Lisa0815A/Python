string = input("Enter a string: ")

count = 0
for char in string:
    if char >= '0' and char <= '9':
        count += 1

print("Number of digits in the string:", count)