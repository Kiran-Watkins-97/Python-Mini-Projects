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
df_merge = pd.merge(df_temp_f, df_rain_f, on='Year', how='inner')
print(df_merge)

# Sort the data by Temperature using the pandas method sort_values, default is asc
df_merge_sort_temp_asc = df_merge.sort_values(by='Temperature')
print(df_merge_sort_temp_asc)
df_merge_sort_temp_desc = df_merge.sort_values(by='Temperature', ascending=False)
print(df_merge_sort_temp_desc)

# Sort the data by Rainfall using the pandas method sort_values, default is asc
df_merge_sort_rain_asc = df_merge.sort_values(by='Rainfall')
print(df_merge_sort_rain_asc)
df_merge_sort_rain_desc = df_merge.sort_values(by='Rainfall', ascending=False)
print(df_merge_sort_rain_desc)


# Synthesize the seaborn window
sns.set(rc={'figure.figsize': (12, 6)})

# Then plot a regression using seaborn jointplot function
sns.jointplot(data = df_merge, x='Rainfall', y='Temperature',  kind='reg')


# Show the scatter pot using the pyplot function show
# Note this shows all currently plotted graphs
plt.show()

Test 1
