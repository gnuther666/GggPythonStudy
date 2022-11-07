import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
print('原始数据\n', df)
ret = df.groupby("A")[["C", "D"]].sum()  # 按A进行分组, 取C/D 两个字段的sum
print('聚合sum\n', ret)
ret2 = df.groupby(['A', 'B']).sum()  # 按A/B 进行分组, 取剩余字段的sum
print('分层聚合\n', ret2)
