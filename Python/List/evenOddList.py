list = [42,3,56,78,91,12,16,24]
even_numbers = []
even_count = 0
for num in list:
  if num%2==0:
    even_numbers.append(num)
    even_count += 1
print("Even numbers:",even_numbers)
print("Count of even numbers:", even_count)
odd_numbers = []
odd_count = 0
for num in list:
  if num%2!=0:
    odd_numbers.append(num)
    odd_count += 1
print("Odd numbers:",odd_numbers)
print("Count of odd numbers:",odd_count)    