import pandas as pd
import numpy as np

s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
print('字符串序列小写\n', s.str.lower())  # 取小写
print('字符串序列大写\n', s.str.upper())  # 取小写
print('字符串序列匹配次数\n', s.str.count('[a-z]', flags=1))  # 统计序列内出现次数 flags 0 常规匹配 1 正则匹配
print('字符串序列匹配值\n', s.str.match('^[a-zA-Z]+$', flags=0))  # 查看序列是否满足匹配 flags 0 正则匹配 1 常规匹配
# 'capitalize', 'casefold', 'cat', 'center', 'contains', 'count', 'decode', 'encode',
# 'endswith', 'extract', 'extractall', 'find', 'findall', 'fullmatch', 'get', 'get_dummies',
# 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'islower', 'isnumeric', 'isspace',
# 'istitle', 'isupper', 'join', 'len', 'ljust', 'lower', 'lstrip', 'match', 'normalize', 'pad',
# 'partition', 'removeprefix', 'removesuffix', 'repeat', 'replace', 'rfind', 'rindex', 'rjust',
# 'rpartition', 'rsplit', 'rstrip', 'slice', 'slice_replace', 'split', 'startswith', 'strip',
# 'swapcase', 'title', 'translate', 'upper', 'wrap', 'zfill'
