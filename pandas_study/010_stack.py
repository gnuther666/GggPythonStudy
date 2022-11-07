import pandas as pd
import numpy as np

tuples = list(
    zip(
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    )
)
print('原始数据\n', tuples)
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
print('原始数据2\n', df[:4])
print('stack数据\n', df[:4].stack())
print('unstack数据\n', df[:4].unstack())
print('unstack数据-parm0\n', df[:4].unstack(0))
print('unstack数据-parm1\n', df[:4].unstack(1))

