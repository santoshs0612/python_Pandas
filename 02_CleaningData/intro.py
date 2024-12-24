# fixing bad Data 
# Bad Datas are ::
# Empty Cell, Darta in wrong formar, Wrong Data, Duplicates 


import pandas as pd 

df = pd.read_csv("data.csv")

# remove empty cells rows 
# returns new Data frames with non empty cells
# newDf = df.dropna()
# print(newDf.info())

# print(newDf.to_string())

#  if we wnat to change the original data Frame 

# df.dropna(inplace=True)
# print(df.to_string())

