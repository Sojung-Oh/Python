import pandas as pd

"""
#결측값
data = {
    "Name": ['홍길동', '임꺽정', '성춘향'],
    "Age": [25, None, 20],
    "City": ['서울', '부산', None]
}

df = pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum()) #결측값 개수 확인
print(df.info()) #간략한 정보 보기

#df_drop = df.dropna() #결측값이 있는 행 삭제
#df_drop_column = df.dropna(axis = 1) #결측값이 있는 열 삭제

#df_fill = df.fillna(0) #데이터 타입에 맞춰서 들어간다
#df_fill_f = df.fillna(method = 'ffill') #이전 값으로 채우기
#df_fill_b = df.fillna(method = 'bfill') #다음 값으로 채우기
#print(df_fill)
"""
"""
# #isin() 메서드
# s = pd.Series(["홍길동", "임꺽정", "성춘향", "이몽룡"])
# result = s.isin(['홍길동', '이몽룡'])
# print(result)

data = {
    'Name': ["홍길동", "임꺽정", "성춘향", "이몽룡"],
    'Age': [25, 30, 20, 32]
}

df = pd.DataFrame(data)
#result = df.isin(['성춘향', '홍길동', 20]) #True/False찾기
result = df[df['Name'].isin(['성춘향', '홍길동', 32])] #Name에서만 찾기 , True 값만 필터링
print(result)

# s = pd.Series([1, 2, None])
# result = s.isin([None, 2])
# print(result)  #결측값을 무시한다

"""
"""
#빈도수

s = pd.Series(['사과', '바나나', '사과', '오렌지', '바나나', '사과'])
print(s.value_counts())

df = pd.DataFrame({
    "과일": ['사과', '바나나', '사과', '오렌지', '바나나', '사과'],
    "수량": [1, 2, 3, 4, 5, 6]
})

#print(df['과일'].value_counts(normalize = True)) #빈도를 비율(%)
print(df['과일'].value_counts(ascending = True)) #오름차순
print(df['과일'].value_counts(dropna=False))
"""

"""
s = pd.Series([1, 2, 3, 4, 5])
result = s.agg(['sum', 'mean', 'max'])
print(result)

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 11, 12]
})
#print(df.agg(['sum', 'mean']))
print(df.agg({'A': 'sum', 'B': 'mean'})) #지정해서
"""

"""
s1 = pd.Series([10, 20, 30])
s2 = pd.Series([5, 15, 25])

print(s1 + s2)
print(s1 - s2)
print(s1 * s2)
print(s1 / s2)
print(s1 > s2)

#통계 연산
print(s1.sum())
print(s1.mean())
print(s1.max())
print(s1.min())
print(s1.std()) #표쥰편차
print(s1.var()) #분산
print(s1.median()) #중앙값
#통계지표
print(s1.describe())
"""

# #그룹

# data = {
#     'group': ['A', 'A', 'B', 'B', 'C'],
#     'value': [10, 20, 30, 40, 50]
# }
# df = pd.DataFrame(data)

# #result = df.groupby('group')['value'].sum()
# result = df.groupby('group')['value'].agg(['sum', 'mean', 'max'])
# print(result)



data = {
    'group': ['A', 'A', 'B', 'B', 'C'],
    'value1': [10, 20, 30, 40, 50],
    'value2': [5, 15, 25, 35, 45]

}
df = pd.DataFrame(data)
result = df.groupby('group').agg({
    'value1': 'sum',
    'value2': ['mean', 'sum']
})

result = df.groupby('group').filter(lambda x : x['value1'].sum() > 30)
print(result)