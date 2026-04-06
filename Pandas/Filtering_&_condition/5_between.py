import pandas as pd
df = pd.DataFrame({
    'A': [10, 20, 30, 40, 50, 60],
})
result = df[df['A'].between(20,50,inclusive='neither')]
print("Filtering rows between 20 and 50 :")
print(result)