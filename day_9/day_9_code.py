#########################################################
#                                                       #
#                      DataFrame                        #
#                                                       #
#########################################################

### Slide 2: Data Input and Output

import pandas as pd

df_csv = pd.read_csv('data.csv')
df_excel = pd.read_excel('data.xlsx')
df_json = pd.read_json('data.json')

df_csv.to_csv('data.csv')
df_excel.to_excel('data.xlsx')
df_json.to_json('data.json')

### Slide 3: Introduction to the Palmer Penguins Dataset

# Load the dataset
penguins = pd.read_csv('penguins.csv')

### Slide 4: Creating a DataFrame from a Dictionary of Lists

d = {"column1": [1., 2., 6., -1.], "column2": [0., 1., -2., 4.]}
df = pd.DataFrame(d)
print(df)

### Slide 5: Creating a DataFrame from a List of Dictionaries

d = [{"a": 1, "b": 2}, {"a": 2, "c": 3}]
df = pd.DataFrame(d)
print(df)

### Slide 6: Getting the Size of a DataFrame

penguins = pd.read_csv('penguins.csv')
n_row, n_col = penguins.shape
print("No. of rows:", n_row, ", No. of columns:", n_col)

### Slide 7: Viewing Data with head()

print(penguins.head(3))

### Slide 8: Viewing Data with tail()

print(penguins.tail(3))

### Slide 9: Summary Statistics

print(penguins[['bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].describe())

### Slide 11: Data Selection and Filtering

print(penguins.loc[0, 'species'])
print(penguins.iloc[0, :])

### Slide 12: Accessing Rows by Index

print(penguins.iloc[10:15])

### Slide 13: Accessing Rows by Condition

print(penguins[penguins['body_mass_g'] > 4000].head())

# In class example: all male penguins of species Adelie

male_adelie = penguins[(penguins['species'] == "Adelie") & (penguins['sex'] == 'male')]


### Slide 14: Accessing Columns by Name

print(penguins['species'].head(3))
print(penguins.species.head(3))

### Slide 15: Accessing Multiple Columns

subset = penguins[['species', 'island']]
print(subset.head())

### Slide 16: A Simple Bar Plot

import matplotlib.pyplot as plt
counts = penguins['species'].value_counts()
counts.plot(kind='bar')
plt.show()

### Slide 17: Handling Missing Values

print(penguins.isnull().sum())
penguins_complete = penguins.dropna()
penguins_filled = penguins.fillna(0)

### Slide 18: Other Useful DataFrame Methods

penguins_deduped = penguins.drop_duplicates()
penguins_renamed = penguins.rename(columns={'species': 'penguin_species'})
print(penguins_renamed.columns)

### Slide 19: Subsetting by notnull() and isnull()

non_null_bill = penguins[penguins.bill_depth_mm.notnull()]
null_bill = penguins[penguins.bill_depth_mm.isnull()]
print(non_null_bill[['rowid', 'bill_depth_mm']].head())
print(null_bill[['rowid', 'bill_depth_mm']].head())

### Slide 20: Data Transformation - Adding and Removing Columns

# Add a new column
penguins['new_column'] = 'value'
# Remove a column
penguins = penguins.drop('new_column', axis=1)

### Slide 21: Applying Functions

penguins['column'].apply(lambda x: x + 1)

### Slide 22: Mapping and Replacing Values

penguins['column'].map({'old_value': 'new_value'})
penguins['column'].replace('old_value', 'new_value')

### Slide 23: Applying to the Penguin Data

def convert_grams_to_lbs(grams):
    return grams / 453.592

penguins['body_mass_lbs'] = penguins['body_mass_g'].apply(convert_grams_to_lbs)
print(penguins[['body_mass_g', 'body_mass_lbs']].head())

### Slide 24: Aggregation and Grouping

grouped = penguins.groupby('species')
print(grouped['body_mass_g'].mean())

### Slide 25: Merging and Joining DataFrames

penguin_egg = pd.read_csv('penguin_egg.csv')
penguin_full = pd.merge(penguins, penguin_egg, on='species')
print(penguin_full.head())

#########################################################
#                                                       #
#             Data Transformation                       #
#                                                       #
#########################################################

### Slide 21: Applying Functions

# Apply a function to a column
df['column'].apply(function)

### Slide 22: Mapping and Replacing Values

# Map values in a column
df['column'].map(mapping_dict)

# Replace values in a column
df['column'].replace(to_replace, value)

### Slide 23: Applying to the Penguin Data

def g_to_lbs(g):
    return g / 453.592

penguins['body_mass_lb'] = penguins['body_mass_g'].apply(g_to_lbs)
print(penguins[['body_mass_g', 'body_mass_lb']].head(3))

### Slide 24: Applying to the Penguin Data

en_zh_map = {
    'Adelie': '阿德利',
    'Chinstrap': '帽带',
    'Gentoo': '巴布亚'
}
scientific_name_map = {
    'Adelie': 'Pygoscelis adeliae',
    'Gentoo': 'Pygoscelis papua',
    'Chinstrap': 'Pygoscelis antarctica'
}

penguins['species_zh'] = penguins['species'].map(en_zh_map)
penguins['species_sci'] = penguins['species'].map(scientific_name_map)

#########################################################
#                                                       #
#             Aggregation and Grouping                  #
#                                                       #
#########################################################

### Slide 26: Aggregation and Grouping

# Group data by one or more columns
grouped = df.groupby('column')

# Aggregate grouped data with various functions
print(grouped['column'].mean())
print(grouped['column'].sum())
print(grouped['column'].count())

### Slide 27: Applying to the Penguin Data

grouped = penguins.groupby('sex')
print(grouped['flipper_length_mm'].mean())
print(grouped['body_mass_g'].mean())

#########################################################
#                                                       #
#          Merging and Joining DataFrames               #
#                                                       #
#########################################################

### Slide 28: Concatenating DataFrames

adelie = pd.read_csv('penguins_adelie.csv')
gentoo = pd.read_csv('penguins_gentoo.csv')
chinstrap = pd.read_csv('penguins_chinstrap.csv')
penguin = pd.concat([adelie, gentoo, chinstrap], axis=0)

### Slide 29: Merging DataFrames

penguin_egg = pd.read_csv('penguin_egg.csv')
penguin_full = pd.merge(penguin, penguin_egg, on='rowid')
print(penguin_full.head())
