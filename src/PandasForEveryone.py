# Source https://learning.oreilly.com/library/view/pandas-for-everyone
# Data https://github.com/chendaniely/pandas_for_everyone
#%%
import pandas as pd
import numpy as np


import pandas as pd

data = [['Rosaline Franklin', '1920-07-25', '1958-04-16', 37, 'Chemist'],
       ['William Gosset', '1876-06-13', '1937-10-16', 61, 'Statistician'],
       ['Florence Nightingale', '1820-05-12', '1910-08-13', 90, 'Nurse'],
       ['Marie Curie', '1867-11-07', '1934-07-04', 66, 'Chemist'],
       ['Rachel Carson', '1907-05-27', '1964-04-14', 56, 'Biologist'],
       ['John Snow', '1813-03-15', '1858-06-16', 45, 'Physician'],
       ['Alan Turing', '1912-06-23', '1954-06-07', 41,
        'Computer Scientist'],
       ['Johann Gauss', '1777-04-30', '1855-02-23', 77, 'Mathematician']]

df = pd.DataFrame(data, columns=['Name', 'Birth Date', 'Death Date', 'Age', 'Occupation'])

print(df)

# %%
names = df['Name']
print(names)
names.to_pickle('output/names.pkl')
# %%
names2 = pd.read_pickle('output/names.pkl')

#####################
# Chapter 3
# %%
import seaborn as sns
anscombe = sns.load_dataset('anscombe')
print(anscombe)

# %%
import matplotlib.pyplot as plt
dataset_1 = anscombe[anscombe['dataset'] == 'I']
dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']

fig = plt.figure()
axes1 = fig.add_subplot(2, 2, 1)
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)
# plt.show()


# fig = plt.figure()
axes1.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')
axes1.set_title('dataset_1')
axes2.set_title('dataset_2')
axes3.set_title('dataset_3')
axes4.set_title('dataset_4')
axes1.set_xlabel('x')
axes2.set_xlabel('x')
axes3.set_xlabel('x')
axes4.set_xlabel('x')
axes1.set_ylabel('y')
axes2.set_ylabel('y')
axes3.set_ylabel('y')
axes4.set_ylabel('y')
fig.suptitle('Anscombe Data')
fig.tight_layout()
plt.show()
# %%

print(dataset_1.isin([dataset_1['x'].mean(), dataset_1['y'].mean()]))
# %%
