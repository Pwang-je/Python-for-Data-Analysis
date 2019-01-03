import pandas as pd
import os
encoding = 'latin1'

# users
upath = os.path.expanduser('C:\\work\\Python for Data Analysis\\dataset\\chapter_test\\users.dat')
# ratings
rpath = os.path.expanduser('C:\\work\\Python for Data Analysis\\dataset\\chapter_test\\ratings.dat')
# movies
mpath = os.path.expanduser('C:\\work\\Python for Data Analysis\\dataset\\chapter_test\\movies.dat')

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

users = pd.read_csv(upath, sep='::', header=None, names=unames, encoding=encoding)
ratings = pd.read_csv(rpath, sep='::', header=None, names=rnames, encoding=encoding)
movies = pd.read_csv(mpath, sep='::', header=None, names=mnames, encoding=encoding)

print('users : \n', users[:5])
print('ratings : \n', ratings[:5])
print('movies : \n', movies[:5])


# todo 나이와 성별에 따른 어떤 영화의 평균 평점 계산하기.

# todo 1. pandas 의 merge 를 이용하여 3개를 하나로 합친다. (ratings 과 users 를 결합 후 그 결과를 movies 와 다시 결합)
datas = pd.merge(pd.merge(users, ratings), movies)
print('Merge data is -\n', datas[:10])
# print(datas.iloc[0])

# todo 2. 성별에 따른 각 영화의 평균 평점을 구하려면 pivot_table 을 사용한다.
mean_ratings = datas.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
print('\nMean ratings is -\n', mean_ratings[:10])




