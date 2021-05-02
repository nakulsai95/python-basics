'''
pandas
pip install pandas
!pip install pandas
''' 

'''
Data 

structured data:      tables, csv, ipl points table
unstructured data      wahtsap conversations 
semi structured data    tweet -> text, retweets, likes , id 
'''

'''
import structured data
perform data cleaning conversations
business analysis
'''

import pandas as pd   #nickname for pandas as pd

#Step 1: importing data to the environment using pandas 

#formats : json, csv, tsv, xlsx, xls, 

#csv, tsv


data = pd.read_csv('datasets/store.csv')
print(data)


#how many android devices has been sold 
#pivot 

#categorical column : text,
#numerical column: number of
#datetime: date 

#data datatype is dataframe 
grouped_data = data.groupby(['Region', 'Store'])['Price'].sum()
grouped_data = pd.DataFrame(grouped_data)
grouped_data = grouped_data.reset_index()
grouped_data = grouped_data.sort_values(by='Price', ascending=False)


#filter a dataframe 
# print(grouped_data[grouped_data['Region'].isin(['West'])])
print(data.iloc[50]) #index location

'''
data frame
table 
columns
values
rows
indexes
'''



# for every region show me sum of price
# print(grouped_data)