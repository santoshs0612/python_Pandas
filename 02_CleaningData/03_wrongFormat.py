import pandas as pd

df = pd.read_csv("data.csv")

# df["Date"]= pd.to_datetime(df["Date"],format="mixed")
# print(df.to_string())

# df.dropna(subset=["Date"], inplace=True)
# print(df.to_string())

# ++++++++Fixing Wrong Data ++++++++++++++

# df.loc[7,"Duration"] =45


# for x in df.index:
#     if df.loc[x,"Duration"]>120:
#         df.loc[x,"Duration"]=120


# for x in df.index:
#     if df.loc[x,"Duration"]>120:
#         df.drop(x,inplace=True)
# print(df)


# +++++++++ Removing Duplicates ++++++++++

print(df.duplicated())

# Remove Duplicates 
df.drop_duplicates(inplace=True)
