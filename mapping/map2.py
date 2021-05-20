import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if ele<=2000:
        return 'green'
    elif ele>2000 and ele<=3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09],zoom_start =6)

fg = folium.FeatureGroup(name = "MyMap")

for lt, ln, ele in zip(lat,lon,elev):
        fg.add_child(folium.CircleMarker(location=[lt, ln], popup=str(ele)+"m", fill_color = color_producer(ele), color = 'grey', fill_opacity =0.7))

fg.add_child(folium.GeoJson(data = open('world.json','r',encoding = 'utf-8-sig').read(), style_function = lambda x:{'fillColor':'yellow'}))
map.add_child(fg)
map.add_child(folium.LayerControl())

map.save("Map1.html")
