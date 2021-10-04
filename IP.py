import os
from urllib.request import urlopen
from geopy.geocoders import Nominatim
import folium
from branca.element import Figure
import socket
import urllib.request
import json
host=input("Enter your target domain : ")
ip=socket.gethostbyname(host)
while True:
    url="http://ipwhois.app/json/"
    response=urllib.request.urlopen(url+ip)
    data=response.read()
    val=json.loads(data)

    print(" Host: "+host)
    print(" IP Address: "+ val['ip'])
    print(" Type: "+ val['type'])
    print(" Country: "+val['country'])
    print(" City: "+ val['city'])
    print(" ISP: "+ val['isp'])
    print(" Organisation: "+ val['org'])
    lat=str(val['latitude'])
    lon=str(val['longitude'])
    print(" Latitude: "+ lat)
    print(" Longitude: "+ lon)
    break

geoLoc = Nominatim(user_agent="GetLoc")
locname = geoLoc.reverse((lat,lon))
print(" Exact address: "+locname.address)
fig=Figure(width=550,height=350)
img=folium.Map(width=550,height=350,location=[lat,lon],zoom_start=11,min_zoom=5,max_zoom=20)
folium.Marker(location=[lat,lon], popup = 'Name:{host}\n Address:{locname}').add_to(img)
img.save('locmap.html')