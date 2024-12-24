import pandas as pd

data = {
    "calories": [420,380,390],
    "Duration": [50,40,30]
}

# load Data into data frame object 
df = pd.DataFrame(data)
# print(df)

#  Use of "loc" attributes to return one or more specified rows
# print(df.loc[0])
# use a list of index
# print(df.loc[[0,1]])

# indexing 
df1 = pd.DataFrame(data,index=["day1","day2","day3"])

# print(df1)
# locate 
# print(df1.loc["day2"])

dfFile = pd.read_csv('data.csv')

print(dfFile)