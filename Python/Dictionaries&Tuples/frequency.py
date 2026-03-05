numbers = [10,20,30,40,10,20,20,40,30,30,30,40]
frequency = {}
for i in numbers:
  if i in frequency:
    frequency[i] += 1
  else:
    frequency[i] = 1
print(frequency)      