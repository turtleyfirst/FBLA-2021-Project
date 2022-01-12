import requests
typeI = 'doctor'
keyword = ''
# accepted types: https://developers.google.com/maps/documentation/places/web-service/supported_types
radius = '10000'
coord1 = '39.5481' #lattitude
coord2 = '-104.9739' #longitude
location = coord1 + '%2C' + coord2 #compiles coordinate into usable
API_KEY = 'AIzaSyCmvD0GGssDQbaKG6U6xscR7p81FqRGmr8' #API access key
url1 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?" + "location=" + location + "&radius=" + radius + "&type=" + typeI + "&keyword=" + keyword + "&key=" + API_KEY

payload={} #bullshit
headers = {} #more bullshit

response = requests.request("GET", url1, headers=headers, data=payload)

print(response.text) #output, can be stored as .json when needed, AKA noah's job
# this part will also return a field called place_id, which can be inputted into a place_details request to return specific data about the location such as consumer reviews