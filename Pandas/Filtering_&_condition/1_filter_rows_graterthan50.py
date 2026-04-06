import pandas as pd
df = pd.DataFrame({
  'name' : ['alice','rysha','bob'],
  'marks' : [60,32,50]
})
result = df[df['marks']>50]
print("Filtering rows greater than 50 :")
print(result)