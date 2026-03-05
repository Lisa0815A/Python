string = input("Enter a string: ")

freq = {}

# Count frequency of each character
for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Find first non-repeating character
for char in string:
    if freq[char] == 1:
        print("First non-repeating character is:", char)
        break
else:
    print("No non-repeating character found.")