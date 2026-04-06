import pandas as pd

df = pd.DataFrame({
    'marks': [40, 60, 80, 30]
})

# replace marks < 50 with "Fail"
df.loc[df['marks'] < 50, 'marks'] = "Fail"
print(df)