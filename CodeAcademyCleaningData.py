import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

files_glob = glob.glob('state*.csv')

df_list = []
for files in files_glob:
  data = pd.read_csv(files)
  df_list.append(data)

us_census = pd.concat(df_list)

#print(us_census.head(5))
#print(us_census.columns)
#print(us_census.dtypes)

us_census['Income'] = us_census['Income'].str.replace('$', '')

us_census_genderpop = us_census.GenderPop.str.split('_', expand = True)

us_census['Men'] = us_census_genderpop.get(0)
us_census['Women'] = us_census_genderpop.get(1)

us_census[['Men', 'Women']] = us_census[['Men', 'Women']].replace('[M|F]*', '', regex = True)

us_census.Men = pd.to_numeric(us_census.Men)
us_census.Women = pd.to_numeric(us_census.Women)
us_census.Women = us_census.Women.fillna(us_census.TotalPop - us_census.Men)

us_census = us_census.drop_duplicates()

plt.scatter(us_census.Women, us_census.Income)
plt.show()

print(us_census.columns)


