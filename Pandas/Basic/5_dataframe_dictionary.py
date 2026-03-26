import pandas as pd 
data = {
  "name": ['john','bob','sam'],
  "age" : [18,23,20],
  "city" : ['bhubaneswar','Delhi','Mumbai']
}
df = pd.DataFrame(data)
print(df) 