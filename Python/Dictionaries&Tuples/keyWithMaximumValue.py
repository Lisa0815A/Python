marks = {
  "a":85,
  "b":90,
  "c":78,
  "d":92,
  "e":88
}
max_key = max(marks ,key=marks.get)
max_value = marks[max_key]
print("Key :", max_key)
print("Value :",max_value)