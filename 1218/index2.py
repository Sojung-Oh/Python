import folium
import requests
from geojson import Feature, FeatureCollection, Point
from folium.plugins import HeatMap
import cv2

#리더님 코드 참고


def get_fire_data():

    features = []

    api_url = "https://eonet.gsfc.nasa.gov/api/v3/events"
    params = {
    "category": "wildfires",
    "status": "open",
    "limit": 100
    } #parameter를 쿼리 스트링으로 넣어도 되고, get의 옵션으로 넣어도 된다

    res = requests.get(api_url, params=params)
    #print(res.json())
    api_data = res.json()
    events = api_data["events"]

    #딕셔너리일 때
    #get()
    #딕셔너리.get(키값, 반환될 값의 타입 또는 값)
    data = {"events": ["이벤트1", "이벤트2"]}
    #print(data.get("events", [])) #예시 코드
    print(data.get("geometry", [{}]))

    for event in events:
        title = event["title"] #팝업창에 타이틀 띄워주기 위해
        geometry = event["geometry"]
        date = geometry[0]["date"] #date = event.get("geometry", [{}])[0].get("date")
        magnitude = geometry[0]["magnitudeValue"] if "magnitudeValue" in geometry[0] else "0.0" #예외처리, geometry magnitudeValue가 존재하지 않으면 0으로 보내기
        features.append(
            Feature(geometry=Point((geometry[0]["coordinates"][0],geometry[0]["coordinates"][1])),
                                   properties = {'name': title, "magnitude": magnitude, "date": date})
        )
    #print(features)
    geojson_data = FeatureCollection(features)
    return geojson_data

#시각화

def fire_map():
    m = folium.Map(location=[42.125210, 73.707073], zoom_start = 5)

    #geojson 데이터 가져오기
    fire_data = get_fire_data()

    folium.GeoJson(
        fire_data,
        name = "화재 데이터",
        tooltip=folium.GeoJsonTooltip(
            fields = ["name", "magnitude", "date"],
            aliases = ["지역명", "면적", "날찌"]
        )
    ).add_to(m)


    heat_data = [
        [feature["geometry"]["coordinates"][1], feature["geometry"]["coordinates"][0]]
        for feature in fire_data["features"]
        if feature["properties"]["magnitude"] != None
    ]
    HeatMap(heat_data).add_to(m)



#fire_map()

#-------------------------이미지 다운
def download_image():
    api_url = "https://wvs.earthdata.nasa.gov/api/v1/snapshot"
    params = {
        "REQUEST": "GetSnapshot",
        "BBOX": "-90, -180, 90, 180",
        "WIDTH": "1920",
        "HEIGHT": "1080",
        "FORMAT": "image/png",
        "LAYERS": "VIIRS_SNPP_CorrectedReflectance_TrueColor",
        "CRS": "EPSG:4326",
        "TIME": "2024-12-01"
    }
    res = requests.get(api_url,params=params)
    print(res)
    with open("./1218/test.png", "wb") as file:
        for chunk in res.iter_content(1024):
            file.write(chunk)

#fire_map()
#download_image()

#----------------opencv
def fire_result():
    image = cv2.imread("./1218/test.png")
    if image is None:
        return
    
    