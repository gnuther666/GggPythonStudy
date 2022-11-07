import pandas as pd
import numpy as np

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print('原始数据\n', df)
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
df['F'] = s1
print('数据列\n', s1)
print('增加一列\n', df)
df.at['2013-01-01', 'A'] = 333
df.iat[1, 2] = 334
print('数值修改\n', df)
df.loc[:, 'G'] = np.array([5] * len(df))
print('数值修改2\n', df)
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
print('数值修改3\n', df1)
print('删除空置\n', df1.dropna(how='any'))
# print('查询空值\n', pd.isna(df1))
print('填充空值\n', df1.fillna(value=334))