import folium
import requests
import pandas as pd

API_KEY = "d3ce236ee4cc0ec006a92390471ce578"

#날씨 데이터 가져오기
def get_weather_data(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=kr"
    res = requests.get(url)
    print(res)
    if res.status_code == 200:
        return res.json()
    else:
        return None
cities = [
    {"name": "서울", "lat":37.551698 , "lon":126.989231 },
    {"name": "부산", "lat":35.191985 , "lon":129.115998 },
    {"name": "대전", "lat":36.341553 , "lon":127.403237 },
    {"name": "대구", "lat":35.871471 , "lon":128.601614 }
]

#날씨 데이터 리스트
weather_data = []


for city in cities:
    data = get_weather_data(city["lat"], city['lon'])
    print(data)
    if data:
        weather_data.append({
            "city": city["name"],
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "latitude": city["lat"],
            "longitude": city["lon"] 
        })

weather_df = pd.DataFrame(weather_data)
print(weather_df)

my_map = folium.Map(location=[36.841375, 127.930471], zoom_start=7)


#마커 추가
for _, row in weather_df.iterrows():
    popip_info = f"""
    <b>도시:</b> {row["city"]}<br />
    <b>온도:</b/> {row["temperature"] - 273.15} ℃<br />
    <b>날씨:</b? {row["weather"]}
    """

    #날씨에 따라서 마커 색상
    icon_color = "blue" if row["temperature"] -273.15 < 0 else "lightblue"

    #마커 생성
    folium.Marker(
        location = [ row["latitude"], row["longitude"]],
        popup = folium.Popup(popip_info, max_width=300), #픽셀 값
        icon = folium.Icon(color=icon_color, icon = "cloud")
    ).add_to(my_map)

    my_map.save("./1217/weathermap_API.html")