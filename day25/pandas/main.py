import pandas as pd

# Practice
# data = pd.read_csv('weather_data.csv')
# print(data)

file_name = '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
output_file_name = 'squirrel_count.csv'
data = pd.read_csv(file_name)
new_data = data.groupby('Primary Fur Color').size()
new_data.name = 'Count'
new_data.to_csv(output_file_name, index=True)