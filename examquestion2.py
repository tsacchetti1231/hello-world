import pandas as pd
pd.read_csv('Cambridge_Salaries.csv')

desc = Cambridge_Salaries.describe() #showing the data, to give an understanding

salary =  Cambridge_Salaries.sum()

grouped = Cambridge_Salaries.groupby('division') #Grouped by division for salaries
eachgroup = grouped.sum()
print('The Total salry for the division is')
print('eachgroup')