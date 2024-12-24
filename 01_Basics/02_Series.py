import pandas as pd

# series one dimensional array holding data of any type
# panda series like column in table


a = [1,2,6,8]
myvar = pd.Series(a)
# print(myvar)
# print(myvar[3])

# naming own labels

myvar= pd.Series(a,index=["a",'b','c','d'])

# print(myvar)
# print(myvar["b"])

# key value like series from dictionary 
calories = {"day1":430,"day2":400,"day3":500}
myvar = pd.Series(calories)
# print(myvar)

myvar1 = pd.Series(calories,index=["day1","day2"])

# print(myvar1)

# ++++++++ Data Frames ++++++++++++++
#

# Multidimensional tables called DataFrames 
# series is like column and a Data Frames is the whole Table 

data = {
    "calories": [420,380,390],
    "Duration": [50,40,30]
}

myData = pd.DataFrame(data);
print(myData)