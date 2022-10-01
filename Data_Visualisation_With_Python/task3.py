import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'tempYearly.csv')
print(df)

sns.set(rc={'figure.figsize': (12,6)})
# sns.scatterplot(data=df, x='Year', y='Temperature')

sns.regplot(x='Rainfall', y='Temperature', data=df)

plt.show()
