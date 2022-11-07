import pandas as pd
import numpy as np

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print('原始数据\n', df)
s = pd.Series([1, 3], index=dates[0:2])
print('序列\n', s)
print('sub\n', df.sub(s, axis='index'))
print(df.apply(np.cumsum))
print('自定义函数1\n', df.apply(lambda x: x.max() - x.min()))
print(s.value_counts())