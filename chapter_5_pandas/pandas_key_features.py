import pandas as pd
from pandas import DataFrame, Series
import numpy as np

# todo 1. 재색인 reindex.
obj_1 = Series([4.5, -6.2, 1.3, -2.8], index=['d', 'a', 'b', 'e'])
print(obj_1)
# d    4.5
# a   -6.2
# b    1.3
# e   -2.8
obj_2 = obj_1.reindex(['a', 'b', 'c', 'd', 'e'])
print('reindex obj_1 \n', obj_2)
# todo TypeError: reindex() takes from 1 to 2 positional arguments but 6 were given
# 이 애러는 index 를 재색인 하는데 [] 로 묶어주지 않아서 생긴다.
# a   -6.2
# b    1.3
# c    NaN
# d    4.5
# e   -2.8


