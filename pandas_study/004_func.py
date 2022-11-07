import pandas as pd
import numpy as np

dates = pd.date_range("20130101", periods=2)
df = pd.DataFrame(np.random.randn(2, 4), index=dates, columns=list("ABCD"))
print('原始数据\n', df)
print('取平均值\n', df.mean())
print('获取单列值\n', df.mean(axis=1))
datas2 = pd.date_range("20130101", periods=6)
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=datas2)
print('查看原始序列\n', s)
print('查看shift属性\n', s.shift(1))