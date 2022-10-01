import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'birthYearly.csv')
print(df)

datap = df.pivot('month', 'year', 'births')
print(datap)

sns.heatmap(datap, annot=True, fmt='d')
plt.show()