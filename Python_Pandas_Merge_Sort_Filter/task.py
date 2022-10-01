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

# Filter the dataframes using query method
df_temp_f = df_temp.query('Temperature < 40 and Temperature > 0')
df_rain_f = df_rain.query('Rainfall < 6 and Rainfall > 0')

# Create scatter plots using the df method plot.scatter
# Pandas .plot documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html
df_temp_f.plot.scatter(x='Year', y='Temperature', label='Temperature by Year')
df_rain_f.plot.scatter(x='Year', y='Rainfall', label='Rainfall by Year')

# Merge the two dataframe using the merge function and with how set to outer
df_merge = pd.merge(df_temp_f, df_rain_f, on='Year', how='outer')
print(df_merge)

# Show the scatter pot using the pyplot function show
# Note this shows all currently plotted graphs
plt.show()

