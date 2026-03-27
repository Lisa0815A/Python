import pandas as pd

data = {
  "name": ['lisa','bob','usha','bichi','pabi'],
  "age": [18,12,13,15,16]
}

df = pd.DataFrame(data)

# Sort by age
df = df.sort_values(by='age')

print("Before reset:\n", df)

# Reset index
df = df.reset_index(drop=True)

print("\nAfter reset:\n", df)