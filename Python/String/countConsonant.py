word = str(input("Enter a word:"))
consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
count = 0
for i in word:
  if i in consonant:
    count += 1
print("Number of consonant in the word:",count)