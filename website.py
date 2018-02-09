import sqlite3
import pandas as pd
import folium
from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster

#form connection
cnx = sqlite3.connect("rentMapRaw.db")

#read the contents of table resumeTable into a pandas dataframe object
#will have 10 columns: first column is the pandas ID (zero-index), second column is the SQL ID (one-index)
df = pd.read_sql_query("SELECT * FROM resumeTable", cnx)

#converts address into coordinates, adds into new coordinates column
nom=Nominatim(scheme="http")
df["coordinates"]=df["address"].apply(nom.geocode)

#pull latitude and longitude from coordinates column, put into their own columns
df["latitude"]=df["coordinates"].apply(lambda x: x.latitude if x !=None else None)
df["longitude"]=df["coordinates"].apply(lambda x: x.longitude if x !=None else None)

#dataframeID = list(df["id"])
companyName = list(df["companyName"])
jobTitle = list(df["jobTitle"])
wantedReq = list(df["wantedReq"])
address = list(df["address"])
salary = list(df["salary"])
avgRent = list(df["avgRent"])
distance = list(df["distance"])
status = list(df["status"])
latitude = list(df["latitude"])
longitude = list(df["longitude"])

map = folium.Map(location=[37.9,-121.3], zoom_start=1, tiles="Mapbox Bright") #map is centered near my home

fgv = folium.FeatureGroup(name="Companies")
marker_cluster = MarkerCluster().add_to(map)

for cName, jTitle, wReq, addr, slry, rent, dst, sts, lat, lon in zip(companyName, jobTitle, wantedReq, address, salary, avgRent, distance, status, latitude, longitude):
    folium.Marker(location=[lat, lon],
    popup=("Company Name: " + str(cName) + "<br>" + "Job Title: " + str(jTitle) + "<br>" + \
    "Wanted Requirements: " + str(wReq) + "<br>" + "Address: " + str(addr) + "<br>" + "Salary: " + \
    str(slry) + "<br>" + "Average Rent: " + str(rent) + "<br>" + "Distance: " + str(dst) + \
    "<br>" + "Application Status: " + str(sts) + "<br>")).add_to(marker_cluster)

map.save("RentMapHTML.html")
