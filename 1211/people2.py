import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
#import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

#폰트 경로찾기
# font_list = font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
# print(font_list)
# path = "C:/Users/HOME/AppData/Local/Microsoft/Windows/Fonts/Pretendard-Medium.ttf"
# #path = "C:\\Users\HOME\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Pretendard-Light.ttf"
# font = font_manager.FontProperties(fname=path).get_name()
# print(font)
# plt.rc('font', family=font)


file_name = './1211/남녀_연령별인구현황.csv' #상대경로
data = pd.read_csv(file_name, encoding='EUC-KR')

region_name = input("검색하고 싶은 지역명을 입력하세요.: ")

#print(data.head())

region_data = data[data['행정구역'].str.contains(region_name, na = False)]
if region_data.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다.")


male_columns = [ col for col in region_data.columns if "남" in col and '세' in col]
female_columns = [ col for col in region_data.columns if "여" in col and '세' in col]

male_columns = [ col for col in region_data.filter(like='남_').columns if '총인구수' not in col and '연령구간인구수' not in col ]
#filter() items = ['2024년11월_남_40~49세', '2024년_남_70~79세]


# for col in male_columns:
#     region_data[col] = region_data[col].astype(str).str.replace(',', '').astype(int)

# for col in female_columns:
#     region_data[col] = region_data[col].astype(str).str.replace(',', '').astype(int)

#이거 대신 판다스의 벡터계산으로 알아서 반복문 돌리도록

male_result = region_data[male_columns].iloc[0].astype(str).str.replace(',', '').astype(int)
female_result = region_data[female_columns].iloc[0].astype(str).str.replace(',', '').astype(int)
female_result = region_data[female_columns].iloc[0].apply(lambda x : int(str(x).replace(',', ''))) #동일한 결과
#apply(): 사용자 함수 정의

age_groups = [col.split('_남_')[1] for col in male_columns]

plt.plot(age_groups, male_result, marker = 'o', label = "남성", color = 'blue')
plt.plot(age_groups, female_result, marker = 'o', label = "여성", color = 'red')

plt.figure(figsize = (10, 8))
plt.plot(age_groups, male_result, marker = 'o', label = region_name)
plt.plot(age_groups, female_result, marker = 'o', label = region_name)
plt.title(f'{region_name}의 연령별 인구 수', fontsize = 16, pad = 10 )
plt.xlabel("연령대")
plt.ylabel("인구수")
plt.grid(True, linestyle = '--', )
plt.xticks(rotation = 45)
plt.legend()

plt.show()

print(age_groups)
