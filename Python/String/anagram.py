str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()

if len(str1) != len(str2):
    print("The strings are not anagrams.")
else:
    freq = {}

    for char in str1:
        freq[char] = freq.get(char, 0) + 1

    for char in str2:
        if char in freq:
            freq[char] -= 1
        else:
            print("The strings are not anagrams.")
            break
    else:
        if all(value == 0 for value in freq.values()):
            print("The strings are anagrams.")
        else:
            print("The strings are not anagrams.")