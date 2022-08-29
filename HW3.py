import pandas as pd

df = pd.read_csv('FoodPrice_in_Turkey.csv')
print(df.head())

df.rename(columns={'Place':'Dia diem','ProductName':'Ten SP'}, inplace=True)
print(df.head())

df['new_column'] = 'NaN'
df.head()

df['Giam gia'] = pd.Series('10%', index = df.index)
df.head()

df.insert(10, 'Giam gia 2', pd.Series('12%', index = df.index))
df.head()

df = df.append({'Dia diem':'NA', 'ProductId':'PR', 'Ten SP':'Rice', 'UmId':10, 'UmName':'KG', 'Month':6, 'Year':2021, 'Price':84.3785, 'Giam gia':'10%', 'Giam gia 2':'12%'}, ignore_index = True)
df.tail()

del df['new_column']
df.head()

df.pop('Giam gia 2')

df.drop('Giam gia', axis = 1, inplace = True)

df.drop(['Month','Year'], axis=1, inplace=True)

# Xoa cac dong trong DataFrame
df.drop(1, axis = 0, inplace=True)

df.drop([7377,7379], inplace=True)



