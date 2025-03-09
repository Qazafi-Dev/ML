import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn import preprocessing, svm 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

df = pd.read_csv('cleaned_data.csv',) 
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
isNull=sum(df.isna().sum())
print ('Total missing values in set after removing duplicates', isNull)
df_filtered = df[(df["Year"] == 2001) & (df["Country"] == "USA")] 
#dispalay the data of year 2001 and country USA
# print(df_filtered) 
df_filtered_coloumns = df.filter(['Country', 'Year','Energy Type','Energy Efficiency Programs'])
isNull_colums=sum(df_filtered_coloumns.isna().sum())
print ('Total missing values in set after removing colums', isNull_colums)
#drop all the columns except the given columns
print('drop all colums except you see from data',df_filtered_coloumns) 
exit()
# ------------------Heat Map-------------------

# Replace NaN with -1 for missing values
df["Energy Efficiency Programs"] = df["Energy Efficiency Programs"].fillna(-1)

# Define vibrant colormap:
cmap = ListedColormap(["grey", "red", "green"])  # Grey for missing (-1), Red for 0, Green for 1

# Create a FacetGrid to generate separate heatmaps for each Energy Type
g = sns.FacetGrid(df, col="Energy Type", col_wrap=2, height=5, sharex=True, sharey=True)

# Function to plot heatmap for each Energy Type
def heatmap(data, **kwargs):
    # Pivot table: Show 1 if any program exists, otherwise 0, and keep -1 for missing data
    heatmap_data = data.pivot_table(values='Energy Efficiency Programs', 
                                    index='Country', 
                                    columns='Year', 
                                    aggfunc=lambda x: 1 if 1 in x.values else 0)
    heatmap_data = heatmap_data.replace({np.nan: -1})  # Mark missing as -1
    
    ax = sns.heatmap(heatmap_data, annot=True, cmap=cmap, linewidths=0.5, cbar=False, **kwargs)
    ax.set_xlabel("Year")
    ax.set_ylabel("Country")

# Apply the function to each facet
g.map_dataframe(heatmap)
g.figure.suptitle('Energy Efficiency Programs by Country and Year for Each Energy Type', y=1.02)

# Add a legend for all heatmaps
legend_patches = [
    Patch(color="grey", label="Missing Data"),
    Patch(color="red", label="No Program (0)"),
    Patch(color="green", label="Has Program (1)")
]
plt.legend(handles=legend_patches, title="Legend", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()
