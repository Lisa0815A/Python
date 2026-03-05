string = str(input("Enter a string:"))
reverse = string[::-1]
if string == reverse:
  print("This string is a pallindrome string.")
else:
  print("This is not a pallindrome string.")  