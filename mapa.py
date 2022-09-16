import folium
import pandas as pd
from geopy.distance import distance
# Creamos el mapa con su centro medellin
centro = [6.238293528532172, -75.57425809266398]
medellin = folium.Map(location=centro, zoom_start=12)
# Ponemos las bodegas y centros comerciales con sus respectivas coordenadas y pines
centros_Comerciales = {"San Diego": [6.2352201801434095, -75.56919415836929],
                       "Viva Envigado": [6.17683453257968, -75.59198797682318],
                       "Mayorca": [6.162177256848752, -75.60544789150312],
                       "Oviedo": [6.199410162677247, -75.57515052102147],
                       "Arkadia": [6.212362873528258, -75.59467318554775],
                       "Premium Plaza": [6.229171673921865, -75.57095707347226],
                       "El Diamante": [6.262035148822235, -75.58999825471531],
                       "Fabricato": [6.3240122320986, -75.5574548248153],
                       "Homecenter-San Juan": [6.249510072876535, -75.5838858116853],
                       "Aventura": [6.26421545052522, -75.56731382424806]}

Bodegas = {"B.Santa Elena": [6.214215444510755, -75.5008635044379],
           "B.Copacabana": [6.357380710065761, -75.50418744957597],
           "B.Caldas": [6.103330226058244, -75.63377336788116],
           "B.Robledo": [6.280276175884955, -75.6003357716567]}

for i in range(len(centros_Comerciales)):
    nombre_Lugar = list(centros_Comerciales.keys())[i]
    lat = list(centros_Comerciales.get(nombre_Lugar))[0]
    lon = list(centros_Comerciales.get(nombre_Lugar))[1]
    folium.Marker(location=[lat, lon], popup=nombre_Lugar,
                  icon=folium.Icon(icon='tag')).add_to(medellin)

for i in range(len(Bodegas)):
    nombre_Lugar = list(Bodegas.keys())[i]
    lat = list(Bodegas.get(nombre_Lugar))[0]
    lon = list(Bodegas.get(nombre_Lugar))[1]
    folium.Marker(location=[lat, lon], popup=nombre_Lugar, icon=folium.Icon(
        color="red", icon='star')).add_to(medellin)

# Mostraremos la distancia entre cada centro comercial y cada bodega
for i in range(len(centros_Comerciales)):
    for j in range(len(Bodegas)):
        nombre_Lugar = list(centros_Comerciales.keys())[i]
        latc = list(centros_Comerciales.get(nombre_Lugar))[0]
        lonc = list(centros_Comerciales.get(nombre_Lugar))[1]
        nombre_Bodega = list(Bodegas.keys())[j]
        latb = list(Bodegas.get(nombre_Bodega))[0]
        lonb = list(Bodegas.get(nombre_Bodega))[1]
        location1 = float(latc), float(lonc)
        location2 = float(latb), float(lonb)
        km = distance([latc, lonc], [latb, lonb])
        folium.PolyLine((location1, location2),
                        popup=(str(km))).add_to(medellin)

# guardamos el mapa en un archivo HTML
medellin.save('index.html')
