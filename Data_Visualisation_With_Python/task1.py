import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json(r'rain.json')

print(df)

print("df statistics", df.describe())

df.plot(x='Month', y='Rainfall')
df.plot(x='Month', y='Temperature')

plt.show()
