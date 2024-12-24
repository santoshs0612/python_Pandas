import pandas as pd 


df = pd.read_csv("data.csv")

# Replace Empty Cells

# df.fillna(130,inplace=True)
# print(df)

# Replace only for Specified Columns 

# df["Calories"].fillna(130,inplace=True)

# print(df)


# Replacement of Data Using Mean Median and Mode
# Mean
x = df["Calories"].mean()

# Meadin

y= df["Calories"].median()

# Mode

z = df["Calories"].mode()[0]

print(x)
df["Calories"] =df["Calories"].fillna(x)
# df["Calories"].fillna({"Calories",x},inplace=True)