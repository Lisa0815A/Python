string = str(input("Enter a sentence:"))
search_word = str(input("Enter a word to search:"))
replace_word = str(input("enter a word to replace:"))
if search_word in string:
  new_string = string.replace(search_word, replace_word)
  print("The new string is:", new_string)
else:
  print("The word is not in the string.")  