import pandas as pd

myDataSet = {
    "Name": "Santosh",
    "Email":"bilok@gmail.com",
    "Age": 16
}
print(myDataSet)
# myValue = pd.Series(myDataSet)

myDataVal = {
    "Cars": ["BYD", "TATA","BMW"],
    "Price":[1,0,-1]
}
# myValue = pd.DataFrame(myDataSet)
# print(myValue)

# print(pd.DataFrame(myDataVal))

print(pd.__version__)