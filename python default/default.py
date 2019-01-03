# todo 함수로 만들고 나중에 append로 추가하기.
def append_element(some_list, element):
    some_list.append(element)
    return append_element


data = [1, 2, 3]
append_element(data, 4)
print(data)


# todo 문자열 포맷을 확인하고, %s를 쓰는법.
a = 4.5
b = 2
print('a is %s, b is %s' % (type(a), type(b)))


# todo 어떤 객체가 무슨 자료형읹지를 알아보는 법. (isinstance)
a = 5
print(isinstance(a, int))


# todo 객체가 리스트인지 검사해서 그렇지 않으면 인자를 변환해주는 방법
def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


data_var = 1
if not isinstance(data_var, list) and isiterable(data_var):
    x = list(data_var)


# todo 문자열 변환법
a = 5.6
print(type(a))      # class 'float'
s = str(a)
print(s, type(s))   # class 'str'


# todo 문자열 템플릿 또는 형식
template = '%.2f %s are worth $%d'
# %s 는 문자열을 인자로 받는 포맷, %.2f 는 소수점 2자리까지, %d 는 일반 정수 포맷.
print(template % (4.5560, 'Argentina', 1))  # 4.56 Argentina are worth $1


x = [4, None, 'foo']
x.extend([7, 8, (2, 3)])
print(x)


# todo enumerate
# https://wikidocs.net/16045
# 반복문 사용 시 몇 번째 반복문인지 확인할 때 사용.
t = [1, 3, 5, 77, 10, 52]
for p in enumerate(t):
    print(p, type(p))
# (0, 1) <class 'tuple'>
# (1, 3) <class 'tuple'>
# (2, 5) <class 'tuple'>
# (3, 77) <class 'tuple'>
# (4, 10) <class 'tuple'>
# (5, 52) <class 'tuple'>

for i, v in enumerate(t):
    print('index : {}, value : {}'.format(i, v))
# index : 0, value : 1
# index : 1, value : 3
# index : 2, value : 5
# index : 3, value : 77
# index : 4, value : 10
# index : 5, value : 52

# todo range;
# range(시작숫자, 종료숫자, step)
range(5)
for i in range(5):
    print(i)






