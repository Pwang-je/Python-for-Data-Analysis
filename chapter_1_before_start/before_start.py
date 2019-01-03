import json
import codecs
import pandas as pd
from pandas import DataFrame, Series
import matplotlib as mpl
import matplotlib.pylab as plt

# coumunity.
# pydata : pandas 와 파이썬 데이터 분석에 관련된 질문을 위한 구글 그룹 리스트.
# pystatemodels : 통계 모델이나 pandas 관련 질문을 올리는 곳.
# scipy-user : 일반적인 scipy나 과학계산 파이썬 관련 질문.

path = 'C:\\work\\Python for Data Analysis\\dataset\\chapter_test\\usagov_bitly_data2012-03-16-1331923249.txt'

f = codecs.open(path, 'r', 'utf-8')
records = [json.loads(line) for line in f]
# print(records[0])

# print(records[0]['tz'])

datas = pd.DataFrame(records)
# print(datas.info())
time_zone = datas['tz'][:10]
print('표준 시간대 : ', time_zone)

time_values = datas['tz'].value_counts()
print('시간 값 : ', time_values.head())

# todo 비어있는 값을 fillna 로 대체 후 matplotlib 으로 그리기.
clean_tz = datas['tz'].fillna('Missing value')  # na 를 missing,
clean_tz[clean_tz == ''] = 'Unknown value'        # 아예 빈 값은 모름으로.
time_values = clean_tz.value_counts()
print('\nclean_tz time values : ', time_values.head(10))

# .plot(kind='barh', rot=0)
plt.plot(time_values[:10])
plt.show()

