# retrieve latitude and longitude of a given location via google maps API
# note - needs an API key first. 

import urllib.request,urllib.parse,urllib.error
import json

#basically a vairable for the first part of the API URL
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
key = ''

while True:
    address = input('Enter a location')
    if len(address) < 1: break
    #concat the serviceurl with the user provided address, encoded to work within a URL (spaces, etc)
    url = serviceurl + urllib.parse.urlencode({'address': address}) + '&key=' + key
    #this is what actually retrieves the data from Google
    uh = urllib.request.urlopen(url)
    # remember, always have to decode
    data = uh.read().decode()

    #again - another try statement in case the service is unavailable or no data is retrieved 
    try:
        js = json.loads(data)
    except:
        js = None
    
    # elegant error if it failed to retrieve.
    if not js or 'status' not in js or js['status'] != 'OK':
        print('Failed to retrieve')

    #pull out just teh bits you need from the json and print
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat:', lat, 'lng:', lng)