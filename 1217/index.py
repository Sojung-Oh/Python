import folium
from geojson import Feature, FeatureCollection, Point, Polygon

# #------지도 열기
# my_map = folium.Map(location = [37.572893, 126.976889], zoom_start = 12)
# my_map.save("./1217/my_map.html")

#------지도 스타일 추가
# my_map = folium.Map(location = [37.572893, 126.976889], zoom_start = 12, tiles = "CartoDB Positron")
# my_map.save("./1217/my_map.html")

# #지도에 마커 추가
# my_map = folium.Map(location = [37.572893, 126.976889], zoom_start = 12, tiles = "CartoDB Positron")

# my_map = folium.Map(
#     location = [37.572445, 126.976924],
#     zoom_start = 12,
#     tiles = "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}"
#     attr = "Google"
# )

# folium.Marker([37.573025, 126.977396], popup = "미국 대사관").add_to(my_map) #기본 마커
# folium.Marker([37.573288, 126.977844], popup = "주한 미국 대사관", icon = folium.Icon(color = 'red', icon = 'hone')).add_to(my_map) 

# #영역 표시
# my_map = folium.Map(location = [37.572893, 126.976889], zoom_start = 13, tiles = "CartoDB Positron")

# #원형 영역
# folium.Circle(location=[37.572574, 126.975651], radius = 500, color = 'blue', popup = '광화문 광장', 
#               fill = True, fill_color = 'yellow').add_to(my_map)

#딕셔너리 형태로 여러 개 추가

# my_map = folium.Map(location=[37.572893, 126.976889], zoom_start = 12, tiles = "CartoDB Positron")

# map_info = [
#     {"location": [37.572574, 126.975651], "popup" : '광화문 광장'},
#     {"location": [37.573288, 126.977844], "popup" : "주한 미국 대사관"},
#     {"location": [37.573025, 126.977396], "popup" : "미국 대사관"}
# ]

# for info in map_info:
#     folium.Marker(
#         location=info["location"],
#         popup=info["popup"],
#         icon = folium.Icon(color='blue', icon="star")
#     ).add_to(my_map)

# my_map.save("./1217/my_map.html")

#-----------------실습
import pandas as pd

# #서울 지하철 5개 위도, 경도
# data = {
#     "Station": ['서울역', "이대역", '충정로역', '아현역', '동대문역사문화공원역'],
#     "Latitude": [37.556078, 37.556923, 37.560188, 37.557484, 37.565798],
#     "Longitude": [126.972264, 126.945803, 126.964163, 126.955681, 127.009710]
# }

# subway = pd.DataFrame(data)
# subway.to_csv("./1217/subway.csv", index = False, encoding="euc-kr")
# #folium 지도 제작
# my_map = folium.Map(location=[37.57, 126.9], zoom_start=10, tiles="CartoDB Positron")

# subway.apply(lambda x : folium.Marker(
#     location=[x["Latitude"], x["Longitude"]],
#     popup = ['Station'],
#     icon = folium.Icon(color = 'blue', icon = 'star')
# ).add_to(my_map), 
# axis = 1
# ) #axis = 1 행단위로 적용한다는 의미
# #iterrow() : 데이터프레임에서 행단위로 반복하면서 인덱스와 행의 쌍을 반환하는 함수
# #---------for 문으로 쓰는 경우
# # for _, x in subway.iterrows():
# #     folium.Marker(
# #         location=[x["Latitude"], x["Longitude"]],
# #     popup = ['Station'],
# #     icon = folium.Icon(color = 'blue', icon = 'star')
# # ).add_to(my_map), 



# my_map.save("./1217/my_map_practice.html")

#--------------------------------------------------------------------------
#geojson
#GeoJson 데이터 생성
"""
feature1 = Feature(geometry=Point((126.989231,37.551698)), properties={"name": "서울", "population": '970만'})
feature2 = Feature(geometry=Point((129.115998,35.191985 )), properties={"name": "부산", "population": '340만'})
feature3 = Feature(geometry=Point((127.403237,36.341553 )), properties={"name": "대전", "population": '150만'})
feature4 = Feature(geometry=Point((128.601614,35.871471 )), properties={"name": "대구", "population": '240만'})

#GeoJson 여러개를 하나로 묶기

geojson_data = FeatureCollection([feature1, feature2, feature3, feature4])

#지도 생성
my_map = folium.Map(location=[36.841375, 127.930471], zoom_start=7)

#GeoJson 데이터 묶은 것을 지도에 추가
folium.GeoJson(
    geojson_data, 
    name = "GeoJSON Data",
    tooltip=folium.GeoJsonTooltip(
        fields = ["name", "population"], #표시할 속성
        aliases = ["도시이름: ", "인구: "] #속성의 별칭
    )
).add_to(my_map)

my_map.save("./1217/my_map_geojson.html")
"""

#----------------------
#실습. GeoJSON 실습

#Polygon 사용하여 지도 위에 다각형 만들 것

#tooltip은 featurecollection에서만 쓸 수 있음

#point = [lon, lat]
point1 = [126.601133, 37.474937]
point2 = [126.685374, 37.948366]
point3 = [127.086375, 38.266057]
point4 = [127.586253, 37.920205]
point5 = [127.490123, 37.707563]
point6 = [127.786754, 37.555301]
point7 = [127.539561, 37.076928]
point8 = [126.938060, 36.949726]
point9 = [126.578258, 37.256401]

feature = {
    "type": 'Feature',
    "geometry": {
        "type": "Polygon",
        "coordinates": [[point1, point2, point3, point4, point5, point6, point7, point8, point9, point1]],
    },
    "properties": {
        "name": "수도권"
    } 
}

geojson_data = FeatureCollection([feature])

#지도 생성
my_map = folium.Map(location=[37.594484, 127.086375], zoom_start=9)

#GeoJson 데이터 묶은 것을 지도에 추가
folium.GeoJson(
    geojson_data, 
    name = "GeoJSON Data",
    tooltip=folium.GeoJsonTooltip(
        fields = ["name"]
    ), 
    style_function=lambda x : {
        'fillColor': "blue", #다각형 내부 색상
        "color": "black", #테두리 색상
        "weight": 2, #테두리 두께
        "fillOpacity": 0.5 #내투 투명도
    }
).add_to(my_map)

my_map.save("./1217/my_map_geojson_practice.html")
# 리더님 코드 참고 