import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("production_data.csv")

productivity = data["units_produced"] / data["workers"]

plt.plot(data["day"], productivity)
plt.xlabel("Day")
plt.ylabel("Productivity (units per worker)")
plt.title("Production Productivity Analysis")
plt.show()
