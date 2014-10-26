##############################################
####	Author: Hunter Gregal		  ####
##############################################

##To Do
##add geolocate by zip ...Google Maps API?
##Crack user ID hash scheme

import requests
import json

#Coords of Town
lat = "44.4758800"
lon = "-73.2120700"

raw = requests.get("https://us-east-api.yikyakapi.net/api/getMessages?lat="+lat+"&long="+lon+"&userID=92C0B0D7EBFDC55AD108F88F67A47D34")
data = json.loads(raw.content)
for x in data["messages"]:
	print "MESSAGE: " + x["message"]
	print "COORDINATES: " + str(x["latitude"]) + "," + str(x["longitude"])
	print "MAP: " + "http://www.google.com/maps/place/"+ str(x["latitude"]) + "," + str(x["longitude"])

