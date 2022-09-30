import pandas as pd

# Create canned data to populate key:value dictionary
data = {"Month": {"0": "January", "1": "February", "2": "March", "3": "April", "4": "May", "5": "June", "6": "July",
                  "7": "August", "8": "September", "9": "October", "10": "November", "11": "December"},
        "Rainfall": {"0": 1.65, "1": 1.25, "2": 1.94, "3": 2.75, "4": 2.75, "5": 3.645,
                     "6": 5.5, "7": 1.0, "8": 1.3, "10": 0.5, "11": 2.3},
        "Temperature": {"0": 3, "1": 10, "2": 15, "3": 20, "4": 25, "5": 24,
                        "6": 30, "7": 1.0, "8": 33, "10": 32, "11": 2.3}
        }

# Create the dataframe using static data
dfs = pd.DataFrame(data)

# Create the dataframe using csv data
dfc = pd.read_csv(r'./data.csv')

# Create the dataframe using JSON data
dfj = pd.read_json(r'./data.json')

# Print the output
print("Static dataframe:")
print(dfs)
print("CSV dataframe:")
print(dfc)
print("JSON dataframe:")
print(dfj)

# This data needs cleaning, so we will want to fill some of it
df = dfc
dfz = df.fillna(0)

# Print cleaned dataframe
print("Cleaned (NaN set to zero) dataframe:")
print(dfz)

# This would skew data too much, so instead we remove rows with invalid data
df = dfc
dfr = df.dropna(0)

# Print cleaned dataframe
print("Cleaned (NaN rows removed) dataframe:")
print(dfr)

# Create a count of all rows that return NaNs
count = 0
for index, row in dfc.iterrows():
    if any(row.isnull()):
        count = count + 1
print("Number of rows removed due to NaNs: " + str(count))

# Find the mean
mean = dfr.mean(numeric_only=True)
print("Mean: \n" + str(mean))

# Find the median
median = dfr.median(numeric_only=True)
print("\nMedian: \n" + str(median))

# Find the Standard Deviation
std = dfr.std(numeric_only=True)
print("\nStandard Deviation: \n" + str(std))

# Find the summary data for just rainfall
mean_rainfall = dfr['Rainfall'].mean()
median_rainfall = dfr['Rainfall'].median()
std_rainfall = dfr['Rainfall'].std()
print("\nRainfall summary:")
print("Mean Rainfall: " + str(mean_rainfall))
print("Median Rainfall: " + str(median_rainfall))
print("Std Rainfall: " + str(std_rainfall))
describe_rainfall = dfr['Rainfall'].describe()
print("\nSecondary method to display summary data:")
print(describe_rainfall)


# Find mean rainfall for first 3 months
rainfall_3m = dfr['Rainfall'][0:3]
print("Rainfall for first 3 months:")
print(rainfall_3m)
print("Mean rainfall over these 3 months: " + str(rainfall_3m.mean()))

# Find mean temperature and rainfall for first 3 months
temp_rain_3m = dfr[['Temperature', 'Rainfall']][0:3]
print("Temperature and rainfall for first 3 months:")
print(temp_rain_3m)
print("Mean temperature and rainfall over these 3 months: \n" + str(temp_rain_3m.mean()))


# Set up an index
index = dfr['Month']
dfi = dfr.set_index(index)

# Find data using the index
print("\nData found using index: ", dfi.loc['March'])

