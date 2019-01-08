from pandas import DataFrame, Series
import pandas as pd
import numpy as np

'''
    1. DataFrame 과 Series 모두 index(색인) 속성을 갖고 있다.
    index 는 제일 왼쪽에 ~기준으로 라고 생각하면 된다. 
    2. 배열에서 값을 선택하거나 대입할 때는 index를 이용해서 접근한다.
    3. DataFrame 은 1차원 이상(2차원이나 3, 4...) 으로 만들어진다. 따라서,
        1차원의 df는 없다.
'''

# todo 1. Series
obj2 = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(obj2)
# a    1
# b    2
# c    3
# d    4

# todo 1-1. dict 도 바로 만들 수 있음.
# dict 타입 데이터를 -> Series()안에 담아서 -> 변수에 할당.
# 만약 Series 에 담지 않고 바로 print로 불러올 시 들어간 데이터 그대로 나온다.
s_data = {'ohio': 35000, 'california': 280000, 'seoul': 100000, 'tokyo': 100000}
obj4 = s_data
print(obj4)
# {'ohio': 35000, 'california': 280000, 'seoul': 100000, 'tokyo': 100000}
obj3 = Series(s_data)
print(obj3)
# ohio           35000
# california    280000
# seoul         100000
# tokyo         100000

# obj3 과 obj5 는 같다.
states = ['busan', 'ohio', 'california', 'seoul']
obj5 = Series(s_data, index=states)
print('\nobj5 = \n', obj5)
# busan              NaN
# ohio           35000.0
# california    280000.0
# seoul         100000.0
# busan이 NaN 으로 나오는 이유는 busa 에 대한 값을 찾을 수 없기 떄문이다.

# todo 1-2. isnull() 과 notnull() 은 누락된 데이터를 찾을 때 사용한다.


# todo 2. DataFrame
data = {'states': ['seoul', 'seoul', 'seoul', 'tokyo', 'tokyo'],
        'year': [2002, 2003, 2004, 2005, 2006],
        'pop': [1.5, 1.7, 2.1, 1.3, 1.2]}
df = DataFrame(data)
print('\ndatafram df = \n', df)
#    states  year  pop
# 0  seoul  2002  1.5
# 1  seoul  2003  1.7
# 2  seoul  2004  2.1
# 3  tokyo  2005  1.3
# 4  tokyo  2006  1.2

# todo 2-1. 순서대로 컬럼을 지정할 수 있음.
# 변수_2 = DataFrame(데이터, columns=['컬럼명1', '컬럼명2', ....])
col_data = DataFrame(df, columns=['year', 'pop', 'states'])
print('\n컬럼명 지정 df \n', col_data)
#     year  pop states
# 0  2002  1.5  seoul
# 1  2003  1.7  seoul
# 2  2004  2.1  seoul
# 3  2005  1.3  tokyo
# 4  2006  1.2  tokyo

# todo 2-2. 없는 값 넘기면 NaN뜨는건 Series 와 마찬가지.
df_2 = DataFrame(df, columns=['year', 'pop', 'states', 'debt'])
print('\nNaN\n', df_2)
#     year  pop states  debt
# 0  2002  1.5  seoul   NaN
# 1  2003  1.7  seoul   NaN
# 2  2004  2.1  seoul   NaN
# 3  2005  1.3  tokyo   NaN
# 4  2006  1.2  tokyo   NaN

# todo 2-3. DataFrame 접근법
print(df['states'], df.states)  # 2개는 같다.

# todo 2-4. 없는 칼럼에 데이터 대입하기.
df_2['debt'] = 15
print(df_2)
#    year  pop states  debt
# 0  2002  1.5  seoul    15
# 1  2003  1.7  seoul    15
# 2  2004  2.1  seoul    15

# todo 2-5. 원하는 index 부분에만 데이터 집어넣기
# 변수_2 = DataFrame([넣을 값1, 넣을 값2, ,,,], index=[인덱스 번호1, 인덱스 번호2, ,,,])
want_data = DataFrame([-1.2, 5, -3.0], index=[0, 2, 4])
df_2['debt'] = want_data
print('\ndebt 의 원하는 index에 데이터 집어넣기\n', df_2)
#     year  pop states  debt
# 0  2002  1.5  seoul  -1.2
# 1  2003  1.7  seoul   NaN
# 2  2004  2.1  seoul   5.0
# 3  2005  1.3  tokyo   NaN
# 4  2006  1.2  tokyo  -3.0

# todo 2-6. 칼럼 삭제.
del df_2['debt']
print(df_2.columns)
# Index(['year', 'pop', 'states'], dtype='object')

# todo 2-7. numpy 와 마찬가지로 변수.T 하면 행열 바뀜.
# todo 2-8. index 직접 지정하는 방법. (index 를 기준으로 원하는 값 알아내기) ''보류
# i_data = DataFrame(df_2['pop'], index=['2003', '2004'])
# print(i_data)
# print('\nindex직접 지정. 여기서는 3\n', i_data)













