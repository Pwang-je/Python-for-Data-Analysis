import pandas as pd
import os
encoding = 'latin1'

upath = os.path.expanduser('C:\\work\\Python for Data Analysis\\dataset\\chapter_test\\u.user')

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']

users = pd.read_csv(upath, sep='::', header=None, names=unames, encoding=encoding)

print(users)









