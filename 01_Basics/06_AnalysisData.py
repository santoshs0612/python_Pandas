import pandas as pd
df = pd.read_csv("data.csv")
# get Quick overview of first 10 datas
# print(df.head(10))
# if will only return first 5 datas 
# print(df.head())

#  Same for the Tail Method 

# print(df.tail())

# Info about data 
print(df.info())