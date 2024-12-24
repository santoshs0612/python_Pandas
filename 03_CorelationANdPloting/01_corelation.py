import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# df.corr()

# print(df.corr())

# df.plot()
# plt.savefig("plot.png")
# plt.show()

# Scatered Plot
# df.plot(kind="scatter", x = "Duration",y="Calories")
# plt.savefig("scatterPlt.png")

# hist plot 

df["Duration"].plot(kind="hist")

plt.savefig("histDuration.png")