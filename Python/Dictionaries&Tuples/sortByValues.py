data = {
    "a": 30,
    "b": 10,
    "c": 20,
    "d": 40
}

sorted_dict = dict(sorted(data.items(), key=lambda x: x[1]))

print(sorted_dict)