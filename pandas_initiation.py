import pandas as pd
import numpy as np

s = pd.Series()
print(s)

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data, index=[100, 101, 102, 103])
print(s)

data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data)
print(s)

data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data, index=['b', 'c', 'd', 'a'], dtype=str)
print(s)

s = pd.Series(5, index=[0, 1, 2, 3])
print(s)

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s[:-3])

df = pd.DataFrame()
print(df)

data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data, columns=['Name','Age'])
print(df)

data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'],
				'Age': [28, 34, 29, 42]}
df = pd.DataFrame(data)
print(df)

data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'],'Age': [28, 34, 29, 42]}
df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
print(df)

data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)

data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print(df)

data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
# With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
# With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])

print(df1)
print(df2)

df = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
			'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
			'three' : pd.Series([10,20,30], index=['a','b','c'])}
df = pd.DataFrame(df)
print(df['one'])
del df['one']
print(df)
print ("Deleting another column using POP function:")
print(df.pop('two'))
print(df)
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
			'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print("info -----")
print(df.info)
print("Head -----")
print(df.head(2))
exit(-2)
print(df.loc['b'])
df = pd.DataFrame(d)
print(df.iloc[2])

df = pd.DataFrame([[1, 2], [3, 4]], columns=['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a','b'])
df = df._append(df2)
# Drop rows with label 0
df = df.drop(0)
print(df)