import numpy as np
import pandas as pd
import matplotlib.pylab as mlt
import scipy.integrate
# 수치적분 루틴과 미분방정식 해법기
import scipy.linalg
# numpy.linalg 에서 제공하는 것보다 더 확장된 선형대수 루틴과 매트릭스 분해
import scipy.optimize
# 함수 최적화기와 방정식의 근을 구하는 알고리즘
import scipy.signal
# 시그널 프로세싱 도구
import scipy.sparse
# 희소 행렬과 희소 선형 시스템 풀이법
import scipy.stats
# 표준 연속/이산 확률 분포(집적도 함수, 샘플러, 연속 분포 함수)와 다양한 통계 테스트, 기술적 통계 도구

import json
import codecs

# coumunity.
# pydata : pandas 와 파이썬 데이터 분석에 관련된 질문을 위한 구글 그룹 리스트.
# pystatemodels : 통계 모델이나 pandas 관련 질문을 올리는 곳.
# scipy-user : 일반적인 scipy나 과학계산 파이썬 관련 질문.

path = 'C:\\work\\Python for Data Analysis\\dataset\\chapter_test\\usagov_bitly_data2012-03-16-1331923249.txt'
f = codecs.open(path, 'r', 'utf-8')
records = [json.loads(line) for line in f]
print(records[0])





