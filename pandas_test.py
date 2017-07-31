import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print s

dates = pd.date_range('20170101', periods=6)
# print dates

df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=list('ABCD'))
# print df

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20170102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
# print 'df2==========================='
# print df2
# print 'df2.dtypes====================================='
# print df2.dtypes
# print 'df.head()=================================='
# print df.head()
# print 'df.tail(3)========================================='
# df.tail(3)

# print df.A
# print df[0:3]
# print df.loc[dates[1]]
# print df.loc[:, ['A', 'B']]
# print df.loc['20170101', ['A', 'B']]
# print df.loc[dates[0], 'A']
# print df.at[dates[0], 'A']
# print df.iloc[3]
# print df.iloc[1:3, 1:3]
# print df.iloc[[1, 2, 4], [0, 2]]
# print df.iloc[: , 1:3]
# print df.iloc[0, 0]
# print df[df > 0]

df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three', ]
# print df2
# print df2[df2['E'].isin(['two', 'three'])]

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20170102', periods=6))
# print s1
df['F'] = s1
df.at[dates[0], 'A'] = 0
df.iat[0, 1] = 0
df.loc[:, 'D'] = np.array([5] * len(df))
# print df
df2 = df.copy()
df2[df2 > 0] = -df2
# print df2

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
# print df1
df1.dropna(how='any')
# print df1
df1.fillna(value='5')
# print df1
# print pd.isnull(df1)
# print df
# print df.mean(1)
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
# print s
# print df
# print df.sub(s, axis='index')
# print df
# print df.apply(np.cumsum)
# print df.apply(lambda x: x.max() - x.min())
s = pd.Series(np.random.randint(0, 7, size=10))
# print s
# print s.value_counts()
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
# print s.str.lower()
df = pd.DataFrame(np.random.randn(10, 4))
print df