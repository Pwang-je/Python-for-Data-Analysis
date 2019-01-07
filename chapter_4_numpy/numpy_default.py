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
print(arr_3d)









