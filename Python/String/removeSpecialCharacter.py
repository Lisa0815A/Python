string = input("Enter a string: ")

result = ""
for char in string:
    if char.isalnum():   # keeps only letters and numbers
        result += char

print("String after removing special characters:", result)