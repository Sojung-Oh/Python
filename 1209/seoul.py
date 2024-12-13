import pandas as pd

file_name = "./1209/서울특별시_공원 내 운동기구 설치 현황_20201231.csv" #파일명 그대로 쓰기
df = pd.read_csv(file_name, encoding = 'cp949')

#print(df.head())  
print(df.info())           
