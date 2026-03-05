numbers = [1,2,3,4,5]
#rotate list element to right
numbers = numbers[-1:] + numbers[:-1]
print(numbers)