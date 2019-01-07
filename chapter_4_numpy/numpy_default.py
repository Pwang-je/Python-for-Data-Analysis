import numpy as np

# todo 1. array 가 중요함.
a_data = np.array([1, 2, 3, 4, 5])
print(a_data)


# todo 2. 색인과 슬라이싱.
arr = np.arange(10)
print(arr)

arr_slice = arr[5:8]
arr_slice[1] = 1231
print(arr)
# [   0    1    2    3    4    5 1231    7    8    9]

# axis 1 은 열을, axis 0 은 행을 이야기함.
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('\narr_3d = \n', arr_3d)

# 슬라이싱은 배열이름[시작 인덱스, 끝 인덱스]
# print(arr_3d[:, 2])


# todo 확인.
# numpy 를 쓸때는 우선 어떻게 되어있는지 확인한다.
test_data = np.arange(0, 15, 2)
print('\ntest_data 확인 = ', test_data)  # [ 0  2  4  6  8 10 12 14]

# 그다음 인덱스의 범위를 확인할 것.
print('\n인덱스 범위 확인. test_data.shape = ', test_data.shape)  # (8,) , 0 <= x < 8 이라는 뜻.

# 배열에 있는 값 읽기.  배열이름[원소값]
print('\n배열 값 읽기 = test_data[3]', test_data[3])  # 6.

for index, a in enumerate(test_data):
    print('for 를 이용한 데이터 확인, test_data[%d]\n' % index, test_data[index], end=', ' )
print('\n')


# todo 불리언 색인 방법.
# todo 정규분포 랜덤 생성 np.random.randn(x, y)
rand_data = np.random.randn(7, 5)
print('rand_data \n', rand_data)


# todo 배열 전치와 축 바꾸기. (행과 열을 바꾼다)
arr_trans = np.arange(15).reshape((3, 5))
print('\narr_trans\n', arr_trans)
# [[0  1  2  3  4]
#  [5  6  7  8  9]
# [10 11 12 13 14]]
print('\narr_trans\n', arr_trans.T)
# [[0 5 10]
#  [1 6 11]
#  [2 7 12]
#  [3 8 13]
#  [4 9 14]]


# todo 통계 메소드 (sum, mean, std, var, min, max cumsum, cumprod)
# todo 정렬. (sort,  arr.sort() )
# todo 중복된 값을 제거하고 남은 값을 정렬된 형태로 반환하기. ( np.unique(value) )
# todo 파일 저장. ( np.save('파일이름') )   :: 파일은 npy 확장자로 저장된다.
# todo 파일 로드. ( np.load('파일이름.npy') )


