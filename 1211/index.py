from pydataset import data
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame

#리더님 코드 참고하기
#print(data())
mtcars = data('mtcars')
#print(mtcars.head())

#종합실습1: 자동차 실린더 수 (cyl)에 따른 평균 연비(mpg)를 계산 후 막대 그래프로 시각화

#sns.barplot(x = 'cyl', y = 'mpg', data = mtcars)
#plt.show()


#종합실습2: 자동차의 변속기 유형(am)별 평균 마력(hp)을 계산한 후 막대 그래프로 시각화

#sns.barplot(x = 'am', y = 'hp', data = mtcars)
#plt.show()

#종합실습3: cyl(실린더 수)을 기준으로 gear(기어 수)에 따른 평균 연비를 계산하는 표를 재생성한 후 히트맵으로 시각화

#pivot = mtcars.pivot(index = "cyl", columns = 'gear', values= 'mpg') #ValueError: Index contains duplicate entries, cannot reshape
#print(pivot)
# sns.heatmap(pivot, annot = True, fmt = 'd')

# plt.show()

#----------------------------------------
#리더님 코드
#1번

#방법1
# cyl_mpg = mtcars.groupby('cyl')['mpg'].mean().reset_index()
# print(cyl_mpg)

# plt.bar(cyl_mpg['cyl'], cyl_mpg['mpg'])

#방법2
#cyl_mpg = mtcars.groupby('cyl')['mpg'].mean()
#cyl_mpg.plot(kind = 'bar')
#plt.xticks(rotation = 0)

#-----------------------------
#변속기 유형별 평균 마력 

# am_hp = mtcars.groupby('am')['hp'].mean()
# # print(am_hp)

# am_hp.plot(kind = 'bar', color = 'green')
# plt.xticks(rotation = 0)

#--------------------------------
#실린더를 기준으로 기어에 따른 평균
# cyl_gear = mtcars.pivot_table(index = 'cyl', columns='gear', values='mpg')
# print(cyl_gear)
# sns.heatmap(cyl_gear, annot=True, fmt = '.2f')

#pivot() 중복된 조합이 있을 경우 오류 발생, 고유한 값이 보장될 때 사용
#pivot_table() 중복된 조합이 있는 경우에도 동작, 실무에 더 적합
#aggfunc = 'mean' 옵션 확인하기, 명시적으로 평균 써주기
#----------------------------------------------------

#corr(method = 'pearson') : 피어슨 상관계수(기본값)
#corr(method = 'spearman') : 스피어만 상관계수
#corr(method = 'kendall') : 켄달의 타우 상관계수

corr_cars = mtcars[ ['mpg', 'hp', 'wt'] ].corr()
sns.heatmap(corr_cars, annot=True)

plt.show()