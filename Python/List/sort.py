"""height = [176,125,178,165,171,169,173]
print(sorted(height)) """

height = [176,125,178,165,171,169,173]
print(height)
n = len(height)
for i in range(n):
  for j in range(0, n-i-1):
    if height[j] > height[j+1]:
      #swap
      height[j],height[j+1] = height[j+1],height[j]
print("height after sorting: ",height)       