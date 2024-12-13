import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
# #폰트 경로찾기
# # font_list = font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
# # print(font_list)
# path = "Pretendard-Medium.ttf"
# font = font_manager.FontProperties(fname=path).get_name()
# plt.rc('font', family=font)

# file_name = './1211/연령별인구현황1.csv' #상대경로
# data = pd.read_csv(file_name, encoding='EUC-KR')


# region_name = input('검색하고 싶은 지역명을 입력하세요: ')
# data = data.rename(columns={'행정구역': '지역명'})
# age_columns = [ col for col in data.columns if '세' in col ]

# print(age_columns)
# print(data.head())
# #숫자로 변환
# for col in age_columns:
#     data[col] = data[col].astype(str).str.replace(",","").astype(int) 
#     #pandas에서의 형변환은 이렇게 해야한다! 주의: 데이터 타입이 다 똑같아야 한다! 중간에 None과 같은 결측값 있어도 안됨

# #필터링
# # contains(): 문자열 데이터 필터링, 특정 패턴을 찾을 때
# # na: 결측값을 포함할지 결정. 기본 값이 True
# #case: 영문의 대소문자 구분. 기본값 True
# region_data = data[ data['지역명'].str.contains(region_name, na = False)] 

# if region_data.empty:
#     print(f"{region_name}의 지역은 존재하지 않습니다.")

# #2024년11월_계_80~89세 [2024년11월, 80~89세]
# #데이터 추출
# age_groups = [col.split("_계_")[1]  for col in age_columns]
# #print(region_data[age_columns].iloc[0])
# #print(region_data[age_columns].iloc[0].values)
# result = region_data[age_columns].iloc[0].values

# #그래프 그리기
# plt.figure(figsize = (10, 8))
# plt.plot(age_groups, result, marker = 'o', label = region_name)
# plt.title(f'{region_name}의 연령별 인구 수', fontsize = 16, pad = 10 )
# plt.xlabel("연령대")
# plt.ylabel("인구수")
# plt.grid(True, linestyle = '--', )
# plt.xticks(rotation = 45)
# plt.legend()

# plt.show()

#print(data.info())
#print(age_groups)
#print(data.head())

#종합 실습2

file2_name = './1211/남녀_연령별인구현황.csv' #상대경로
data2 = pd.read_csv(file2_name, encoding='EUC-KR')

print(data2.head())
print(data2.info())

region_name = input('검색하고 싶은 지역명을 입력하세요: ')
data2 = data2.rename(columns={'행정구역': '지역명'})
age_columns = [ col for col in data2.columns if '세' in col ]

print(age_columns)

# #숫자로 변환
for col in age_columns:
    data2[col] = data2[col].astype(str).str.replace(",","").astype(int) 
    #pandas에서의 형변환은 이렇게 해야한다! 주의: 데이터 타입이 다 똑같아야 한다! 중간에 None과 같은 결측값 있어도 안됨

#필터링
# contains(): 문자열 데이터 필터링, 특정 패턴을 찾을 때
# na: 결측값을 포함할지 결정. 기본 값이 True
#case: 영문의 대소문자 구분. 기본값 True
region_data2 = data2[ data2['지역명'].str.contains(region_name, na = False)] 

if region_data2.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다.")

#2024년11월_계_80~89세 [2024년11월, 80~89세]
#데이터 추출
#남녀 데이터 나누기 필요

m_region_data2 = region_data2[]



age_groups = [col.split("_계_")[1]  for col in age_columns]
#print(region_data[age_columns].iloc[0])
#print(region_data[age_columns].iloc[0].values)
result = region_data2[age_columns].iloc[0].values

#그래프 그리기
plt.figure(figsize = (10, 8))
plt.plot(age_groups, result, marker = 'o', label = region_name)
plt.title(f'{region_name}의 연령별 인구 수', fontsize = 16, pad = 10 )
plt.xlabel("연령대")
plt.ylabel("인구수")
plt.grid(True, linestyle = '--', )
plt.xticks(rotation = 45)
plt.legend()

plt.show()

