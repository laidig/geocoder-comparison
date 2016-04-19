import httplib2
import json
import os
import urllib

from geopy.geocoders import GoogleV3, GeocoderDotUS, Bing
from geopy import Point

http = httplib2.Http()

bounds = [40.4774,-74.2589,40.9176,-73.7004]

def google(query):
    g = GoogleV3()
    try:
        address, (lat, lng) = g.geocode(query, bounds=bounds)
        return address, (lat, lng)
    except:
        return None, None

def geocoderdotus(query):
    us = GeocoderDotUS()
    try:
        place, (lat, lng) = us.geocode(query)
        return place, (lat, lng)
    except:
        return None, None

def bing(query):
	p = Point((bounds[0]+bounds[2]/2,(bounds[1]+bounds[3])/2))
	b = Bing( os.environ.get('BING_API_KEY'))
	try:
		place, (lat, lng) = b.geocode(query, user_location=p)
		return place, (lat, lng)
	except:
		return None, None

def nominatim(query):
    BASE = "http://nominatim.openstreetmap.org/search?"
    box = ','.join([bounds[1],bounds[2],bounds[3],bounds[0]])
    params = {
        'format': 'json',
        'q': query,
	'bounded':1,
	'viewbox': box
    }
    url = BASE + urllib.urlencode(params)
    r, c = http.request(url)
    c = json.loads(c)
    try:
        result = c[0];
        return result['lat'], result['lon']
    except (KeyError, IndexError), e:
        return None, None

def nycgeoclient(query):
	BASE = "https://api.cityofnewyork.us/geoclient/v1/search.json?"
	params = {
		'input' : query,
		'app_id': os.environ.get('GEOCLIENT_APP_ID'),
		'app_key': os.environ.get('GEOCLIENT_APP_KEY')
	}
	url = BASE + urllib.urlencode(params)
	r, c = http.request(url)
	try:
		c = json.loads(c)
		result = c['results'][0]['response'];
		return result['latitude'], result['longitude'], result['firstBoroughName']
	except (KeyError, IndexError), e:
		print c
        	return None, None

def pelias(query):
	BASE = "http://pelias.mapzen.com/v1/search?"
	params = {
		'api_key': os.environ.get('MAPZEN_KEY'),
		'text' : query,
		'boundary.rect.min_lat': bounds[0],
		'boundary.rect.min_lon': bounds[1],
		'boundary.rect.max_lat': bounds[2],
		'boundary.rect.max_lon': bounds[3]
	}
        url = BASE + urllib.urlencode(params)
        r, c = http.request(url)
        c = json.loads(c)
        try:
		result = c['features'][0]
		return result['geometry']['coordinates'][1],  result['geometry']['coordinates'][0], result['properties']['label']
	except :
		return None, None

