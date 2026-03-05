def count_vowels(text):
    count = 0
    for char in text:
        if char in "aeiouAEIOU":
            count += 1
    return count


string = input("Enter a string: ")
result = count_vowels(string)

print("Number of vowels:", result)