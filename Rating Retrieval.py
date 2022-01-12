import requests
placeId = "ChIJN1t_tDeuEmsRUsoyG83frY4" #example place_id
API_KEY = 'AIzaSyCmvD0GGssDQbaKG6U6xscR7p81FqRGmr8' #API access key
url1 = "https://maps.googleapis.com/maps/api/place/details/json?&place_id=" + placeId + "&fields=rating&key=" + API_KEY
payload={} #bullshit
headers = {} #more bullshit

response = requests.request("GET", url1, headers=headers, data=payload)

print(response.text)