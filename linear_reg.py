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
isNull=sum(df.isna().sum()) #checking null valus in data file and taking their sum
print ('Total missing values in set', isNull)
isDuplicate= df[df.duplicated(['Country', 'Year','Energy Type'])].sort_values('Year') #checking duplicate values in data file and taking their sum
print ('Total duplicate values in set', len(isDuplicate.index))



