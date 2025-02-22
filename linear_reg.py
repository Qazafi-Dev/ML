import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn import preprocessing, svm 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
df = pd.read_csv('energy.csv') 
df_binary = df[['Country', 'Year']] 

# Taking only the selected two attributes from the dataset 
df_binary.columns = ['Con', 'Yrs'] 
#display the first 5 rows 

print(df_binary.head())
#plotting the Scatter plot to check relationship between Sal and Temp 
sns.lmplot(x ="Con", y ="Yrs", data = df_binary, order = 2, ci = None) 
plt.show()
