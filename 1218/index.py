import folium
import requests
import pandas as pd
from folium.plugins import HeatMap
import cv2 


#NASA API로 산불 발생 데이터 수집

params = {
    "category": "wildfires",
    "status": "open"
}

def get_wildfire_data():
    api_url = "https://eonet.gsfc.nasa.gov/api/v3/events"
    res = requests.get(api_url, params = params)
    if res.status_code == 200:
        return res.json()
    else:
        return None


map = folium.Map(
    max_bounds=True,
    min_zoom=2,
    min_lat=-84,
    max_lat=84,
    min_lon=-175,
    max_lon=187
)

data = get_wildfire_data()
#print(data)

events = data["events"]
coords = []

for event in events:
    coord = [event['geometry'][0]['coordinates'][1], event['geometry'][0]['coordinates'][0]] #lon, lat -> lat, lon
    print(coord)
    coords.append(coord)

HeatMap(
        data = coords
    ).add_to(map)


map.save("./1218/wildfire_API.html")

