sentence = str(input("Enter a sentence:"))
count = 0
for i in sentence:
  if i == " ":
    count +=1
print("Number of words in the sentence :",count+1)      