import pandas as pd
import os
data = {
  'name' : ['Alice', 'Bob', 'Charlie'],
  'marks' : [90, 80, 75]  
}
df = pd.DataFrame(data)
df.to_excel('students.xlsx', index=False)
print(os.getcwd())
df = pd.read_excel('students.xlsx')