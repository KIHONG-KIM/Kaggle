# 주요 모듈 import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8')
# print(plt.style.available)
sns.set(font_scale=2.5)

import missingno as msno

# 데이터 셋 확인
df_train = pd.read_csv('input/train.csv')   # pandas 모듈을 사용, red_csv()함수를 통해 csv파일을 읽어와 df_train에 할당
df_test = pd.read_csv('input/test.csv')     # pandas 모듈을 사용, red_csv()함수를 통해 csv파일을 읽어와 df_train에 할당

print(df_train.head())                      # 읽어온 파일의 윗부분 head 5행을 읽어오기
print(df_train.tail())
print(df_train.describe())
# describe()는 누락된 데이터(NaN)은 제외하고 데이터 요약이 진행.
# std 뜻: standard deviation 표준편차

# 1 Null data check
print(df_train.columns)

for col in df_train.columns:
    msg = 'column: {:>10}\t Percent of NaN value: {:.2f}%'.format(col, 100 * (df_train[col].isnull().sum() / df_train[col].shape[0]))
    print(msg)

# 문자열 정렬하기 {:>10} 의미 : 10문자를 오른쪽 정렬하고싶다.

print()

for col in df_test.columns:
    msg = 'column: {:>10}\t Percent of NAN value: {:.2f}%'.format(col, 100 * (df_test[col].isnull().sum() / df_test[col].shape[0]))
    print(msg)

print(df_train[col].shape[0])