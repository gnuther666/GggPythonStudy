import pandas as pd
import numpy as np

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
print('原始数据\n', df2)
df2.to_csv('015_df2.csv')

df2_csv_tmp = pd.read_csv('015_df2.csv')
print('读入csv数据\n', df2_csv_tmp)

df2.to_hdf('015_df2.h5', 'df')

df2_hdf_tmp = pd.read_hdf('015_df2.h5', 'df')
print('读入hdf数据\n', df2_hdf_tmp)