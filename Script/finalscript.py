import requests
import pandas as pd
import hashlib
from pathlib import Path
import gzip
import io

grocery_url = "https://data.cityofchicago.org/resource/3e26-zek2.csv"

params = {"$limit": 50000}

response = requests.get(grocery_url, params=params)

with open("grocery_data.csv", "wb") as f:
  f.write(response.content)

grocery_df = pd.read_csv('grocery_data.csv')

grocery_df

income_df = pd.read_csv('ChicagoZipMedian.csv')
income_df

median_income_df = income_df[income_df['Label (Grouping)'] == 'Median income (dollars)']
median_income_df

households_only_df = median_income_df[[col for col in median_income_df.columns if '!!Households!!' in col or col == 'Label (Grouping)']]

households_only_df

final_households_df = households_only_df[[col for col in households_only_df.columns if 'Margin of Error' not in col]]

final_households_df

final_households_df.columns = [col.split()[-1].split('!!')[0] if 'ZCTA5' in col else col for col in final_households_df.columns]
final_households_df

new_final_household_df = final_households_df.melt(
    id_vars = ['Label (Grouping)',],
    var_name='zip',
    value_name='median_income'
)

newdf = new_final_household_df.drop(columns = 'Label (Grouping)')
newdf



grocery_df['zip'] = grocery_df['zip'].astype(str).str[:5]
grocery_df['store_name'] = grocery_df['store_name'].str.lower()
grocery_df['address'] = grocery_df['address'].str.lower()
grocery_df = grocery_df.drop(columns = ['last_updated', 'location'], errors='ignore')

grocery_df

merged_df = pd.merge(grocery_df, newdf, on='zip', how='left')
merged_df['median_income'] = (
    merged_df['median_income']
    .str.replace(',', '')
    .apply(pd.to_numeric, errors='coerce')
)
merged_df

merged_df = merged_df[merged_df['new_status'] != 'CLOSED']
merged_df

income_group_df = merged_df.groupby('median_income').size().reset_index(name='store_count')
income_group_df = income_group_df.sort_values('median_income')
income_group_df

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.hist(merged_df['median_income'].dropna(), bins=20, color='blue', edgecolor='black')
plt.xlabel('Median Income')
plt.ylabel('Frequency Of Resturuant')
plt.title('Distribution of Median Income')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.scatterplot(data=income_group_df, x='median_income', y='store_count',
                color='#4e79a7', s=80, alpha=0.8)

plt.title('Relationship Between Median Income and Store Count')
plt.xlabel('Median Household Income (USD)')
plt.ylabel('Number of Stores')
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()

import os

print(os.listdir())

grocery_df.to_csv('grocery_df_cleaned.csv', index = False)

final_households_df.to_csv('final_household_df_cleaned.csv', index = False)

merged_df.to_csv('merged_df.csv', index = False)

income_group_df.to_csv('number_of_stores_grouped_by_median.csv', index = False)

