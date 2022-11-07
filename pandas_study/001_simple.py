import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print('带索引的表\n', df)

df2 = pd.DataFrame(
    {
        'A': 1.0,
        'B': pd.Timestamp('20201013'),
        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
        'D': np.array([3] * 4, dtype='int32'),
        'E': pd.Categorical(['test', 'train', 'test', 'train']),
        'F': 'foo'
    }
)
print(df2)
print('dtypes', df2.dtypes)
print(df2.head(3))
print(df2.tail(3))
print(df2.index)
print(df2.to_numpy())
print(df2.describe())
print('转置\n', df2.T)
df3 = pd.DataFrame(
    {
        'A': ['a', 'b', 'c', 'd', 'e'],
        'B': [88, 50, 93, 62, 90]
    }
)
print('排序索引\n', df3.sort_index(axis=1, ascending=True))
print('排序数值\n', df3.sort_values(by='B', ascending=True))

print('获取数据,按切片\n', df[0:3])
print('获取数据,按索引\n', df['2013-01-03': '2013-01-05'])
print('获取字段\n', df.loc['2013-01-03': '2013-01-05', ['A', 'B']])
print('获取字段,按位置编号\n', df.iloc[1])
