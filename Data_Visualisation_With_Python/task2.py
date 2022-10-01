import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_json(r'rain.json')

plt.figure(figsize=(15, 5))
plt.plot(df['Month'], df['Temperature'], label='Temperature')

plt.figure(figsize=(15, 5))
plt.plot(df['Month'], df['Rainfall'], label='Rainfall')

plt.figure(figsize=(15, 5))
plt.plot(df['Month'], df['Temperature'], label='Temperature')
plt.plot(df['Month'], df['Rainfall'], label='Rainfall')
plt.legend()
plt.show()
