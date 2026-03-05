word = str(input("Enter a word :"))
vowels = "aeiouAEIOU"
count = 0
for i in word:
  if i in vowels:
    count = count +1
print("number of vowels in the word is :",count)