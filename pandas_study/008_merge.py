import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(2, 3), index=['A', 'B'], columns=['C1', 'C2', 'C3'])
df2 = pd.DataFrame(np.random.randn(2, 3), index=['A', 'C'], columns=['C4', 'C5', 'C6'])
df3 = pd.DataFrame(np.random.randn(2, 3), index=['A', 'B'], columns=['C4', 'C5', 'C6'])


print('df1\n', df1)
print('df2\n', df2)
print('合并两个表\n', pd.concat([df1, df2]))  # 合并两个表,就是把一个表放到另一个表后边
print('连接两个表\n', pd.merge(left=df1, right=df2, how='left', left_index=True, right_index=True))
print('合并两个表\n', df1.append(df3, ignore_index=True))


