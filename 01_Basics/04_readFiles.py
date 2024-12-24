import pandas as pd

# Read CSV files (comma Seperated Files)

df  = pd.read_csv("data.csv")

# print(df)
#  to display all data 
# print(df.to_string())

# max_row
# limit of system to print data 
# print(pd.options.display.max_rows)

# set limit to display
pd.options.display.max_rows = 9999

df = pd.read_csv("data.csv")
# print(df)

# +++++++++++ Reading Json ++++++++++++++++++++++++++

