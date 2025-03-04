import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn import preprocessing, svm 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
df = pd.read_csv('energy.csv',) 
# print(df.head())
df.columns = df.columns.to_series().apply(lambda x: x.strip())

# print(df.columns)
print('No. of records in dataset: ', len(df.index))
print('No. of columns in dataset: ', len(df.columns))

isNull=sum(df.isna().sum())
 #checking null valus in data file and taking their sum
print ('Total missing values in set', isNull)

isDuplicate= df[df.duplicated(['Country', 'Year','Energy Type'])].sort_values('Year') 
#checking duplicate values in data file and sorting them by year
print ('Total duplicate values in set', len(isDuplicate.index))

df.drop_duplicates(subset=['Country', 'Year','Energy Type'], keep='first', inplace=True)
 #droping duplicate value from data file
print('totla filter values after removing duplicates',len(df.index))

df_filtered = df[(df["Year"] == 2001) & (df["Country"] == "USA")] 
#dispalay the data of year 2001 and country USA
# print(df_filtered) 
df_filtered_coloumns = df_filtered.filter(['Country', 'Year','Energy Type','Energy Efficiency Programs'])
#drop all the columns except the given columns
print('drop all colums except you see from data',df_filtered_coloumns)



g = sns.FacetGrid(df, col="Energy Type", col_wrap=2, height=5)



def heatmap(data, **kwargs):
    heatmap_data = data.pivot_table(values='Energy Efficiency Programs', 
                                    index='Country',  
                                    columns='Year', 
                                    aggfunc=lambda x: 1 if 1 in x.values else 0)
    sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", linewidths=0.5, cbar=False, **kwargs)

# Apply the function to each Energy Type
g.map_dataframe(heatmap)
g.figure.suptitle('Energy Efficiency Programs by Country and Year for Each Energy Type', y=1.02)
plt.show()

