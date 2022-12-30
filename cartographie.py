#python -m notebook access  a jupyter notebook
# run the code in jupter notebook
import pandas as pd
import folium
location='./lillios.csv'
restaurant_location=pd.read_csv(location)
resto_location=restaurant_location[["Latitude", "Longitude", "Name"]]
map = folium.Map(location=[resto_location.Latitude.mean(),resto_location.Longitude.mean()], zoom_start=14, control_scale=True)

for index, location_info in resto_location.iterrows():
    folium.Marker([location_info["Latitude"], location_info["Longitude"]], popup=location_info["Name"]).add_to(map)
