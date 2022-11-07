import pandas as pd
import numpy as np

date_index = ['2022-10-0' + '%s' % (one_date + 1) for one_date in range(0, 9)]
user_coll = ['User_%s' % (one_date + 1) for one_date in range(0, 9)]
scrole = [60, 30, 26, 50, 99, 85, 63, 97, 42]

df = pd.DataFrame({
    'date_index': date_index,
    'user_coll': user_coll,
    'scrole': scrole
})

print('原样数据\n', df)
print('数据过滤\n', df[(df['scrole'] < 80) & (df['scrole'] > 60)])
print('数据过滤: in操作\n', df[df['user_coll'].isin(['User_1', 'User_2'])])
print('数据过滤: 多条件\n', df.query("(scrole >= 60) & (date_index>= '2022-10-04')"))
print('数据过滤: like\n', df[df['user_coll'].str.contains('^User.*$')])