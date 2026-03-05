'''list = [41,2,25,63,44,85]
numbers = set(list)
largest = max(numbers)
numbers.remove(largest)
second_largest = max(numbers)
print("The second largest number is:",second_largest)'''
numbers = [10, 20, 4, 45, 99]

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest number:", second_largest)