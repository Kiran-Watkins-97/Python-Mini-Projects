import pandas as pd
import matplotlib
import seaborn as sns
from matplotlib import pyplot as plt

# Create dataframe using read_csv
df_temp = pd.read_csv(r'tempYearly.csv')
df_rain = pd.read_csv(r'rainYearly.csv')

# Print the dataframe to check over them
print(df_temp)
print(df_rain)

# Create scatter plots using the df method plot.scatter
# Pandas .plot documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html
df_temp.plot.scatter(x='Year', y='Temperature', label='Temperature by Year')
df_rain.plot.scatter(x='Year', y='Rainfall', label='Rainfall by Year')

# Show the scatter pot using the pyplot function show
# Note this shows all currently plotted graphs
plt.show()
