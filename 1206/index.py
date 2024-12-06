import pandas as pd


# #리스트형식으로 생성
# data = [10, 20, 30, 40] #리스트기 때문에 데이터 형식 마음대로 넣어도 된다
# #series =pd.Series(data)
# series = pd.Series(data, index = ["a", "b", "c", "d"])
# print(series)

# #딕셔너리 형식으로 생성
# data = {
#     "a": 10,
#     "b": True,
#     "c": 3.14,
#     "d": "python"
# }

# series = pd.Series(data, name = "딕셔너리")
# print(series) #문자랑 섞여 있어서 데이터 object type
# print(series.index)
# print(series.values)
# print(series.shape)

#튜플 형태로
# data = ('민지', '여', False)
# member = pd.Series(data, index = ['이름', '성별', '결혼여부'])
# print(member)
# print(member['이름']) #인덱스 값으로 접근
# print(member[['성별', '결혼여부']])  # 2x2 행렬 만들어 주어야!

# data = [10, 20, 30, 40, 50]
# series = pd.Series(data, index = ['a', 'b', 'c', 'd', 'e'])
# #print(series[0]) #접근은 가능하지만 인덱스 값을 바꿨으니까 이런 식으로 쓰지 말 것
# print(series[series > 20])
# series['c'] = 100
# print(series)

#실습1. 시리즈 만들기

# data = ('4 cups', '1 cup', '2 large', '1 can')
# product = pd.Series(data, index = ['밀가루', '우유', '계란', '참치캔'], name = 'Dinner')
# print(product)

#데이터 프레임

# data = {
#     'Name': ['홍길동', '임꺽정', '성춘향'],
#     'Age' : [25, 30, 27],
#     'city' : ['서울', '부산', '인천']
# }

# df = pd.DataFrame(data)
# print(df)

# index = ['2020', '2021', '2022', '2023', '2024', '2025']

# yeonghee = pd.Series([140, 150, 160, 170, 180, 190], index = index) #index option
# cheolsu = pd.Series([200, 210, 220, 230, 240, None], index = index) #동일한 인덱스를 가지는 시리즈 2개

# result = pd.DataFrame({
#     '영희': yeonghee,
#     '철수': cheolsu
# })

#print(result)
# print(result.head()) #상위 5개의 데이터 조회
# print(result.tail()) #하위 5개의 데이터 조회
# print(result.shape)
# print(result.info())
# print(result.columns)
# print(result.values)
# print(result.index)
# print(result.dtypes)
# print(result['철수'])
# print(result[['철수']]) #둘의 차이 잘 알아두기!



# data = {
#     'Name': ['홍길동', '임꺽정', '성춘향'],
#     'Age' : [25, 30, 27],
#     'city' : ['서울', '부산', '인천']
# }

# df = pd.DataFrame(data, index=['a', 'b', 'c'])
#print(df)
#print(df.loc['b'])
# print(df.loc['b', 'Age'])
# print(df.loc['a':'c', 'NAme':'Age'])
# print(df.loc[df['Age'] >= 30])
# # print(df.loc[:, 'Name']) # : 은 모든 행 가져오라는 의미!
# # print(df.loc['a', :]) # a행에 있는 모든 열을 가져와라!

# print(df.iloc[1])
# print(df.iloc[1,1])
# print(df.iloc[0:2, 0:2]) #끝값 포함 안됨
# print(df.iloc[[0,2], [1,2]])
# print(df.iloc[:, 0])
# print(df.iloc[0, :])


# data = {
#     'Name': ['홍길동', '임꺽정', '성춘향'],
#     'Age' : [25, 30, 27],
#     'City' : ['서울', '부산', '인천']
# }

# df = pd.DataFrame(data)

# #행 추가
# new_data = {'Name': '이몽룡', 'Age': 31, 'City': '포항'}
# result = pd.concat([df, pd.DataFrame([new_data]) ], ignore_index = True) #합칠 때 쓰는 메서드
# print(result) #인덱스 값이 다시 0이 되었다! 옵션 추가해야함!

# #열 추가
# result["직업"] = ["엔지니어", '개발자', '디자이너', '기획자']
# print(result)

# #요소 값 수정
# result.at[1, 'City'] = '천안'
# result.loc[result['Name'] == "임꺽정", "Age"] = 32
# # print(result)

# #칼럼 변경
# result.rename(columns={'Name' : '이름', 'Age': '나이'}, inplace = True) #원본에 있는 데이터를 변경하겠다는 의미의 옵션
# #print(result)

# #데이터 정렬
# result.sort_values(by='나이', inplace=True, ascending=False) #ascending = True가 기본값, 오름차순, false면 내림차순
# #print(result)

# #칼럼 삭제
# result.drop(columns=['City'], inplace=True)
# #print(result)

#실습2. 데이터 프레임 만들기

data = {
    '이름': ['홍길동', '임꺽정', '성춘향'],
    '수학' : [85, 90, 78],
    '영어' : [88, 76, 92],
    '과학' : [95, 89, 84]
}

df = pd.DataFrame(data)
#print(df)

#Total 열 추가

df['Total'] = [268, 255, 254]

#이몽룡 행 추가
new_data = {'이름': '이몽룡', '수학': 88, '영어':85, '과학': 90, 'Total': 263}
df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
#열 이름 변경
df.rename(columns={'수학':'Math'}, inplace=True)
#요소값 변경
df.at[1,'영어'] = 80
print(df)   #Total값을 다른 열들 값 더해서 구하는 식으로 하는게 더 간단할 수도!