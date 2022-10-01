import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'tempYearly.csv')
print(data)

sns.jointplot(data, x='Rainfall', y='Temperature', kind='hex')
plt.show()
