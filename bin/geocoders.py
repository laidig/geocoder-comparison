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
        place, (lat, lng) = g.geocode(query, bounds=bounds)
        return place, (lat, lng)
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
	p = Point(bounds[0],bounds[1])
	b = Bing( os.environ.get('BING_API_KEY'))
	try:
		place, (lat, lng) = b.geocode(query, user_location=p)
		return place, (lat, lng)
	except:
		return None, None

def mapquest(query):
    BASE = "http://open.mapquestapi.com/nominatim/v1/search?"
    params = {
        'format': 'json',
        'q': query
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
	c = json.loads(c)
	try:
		result = c['results'][0]['response'];
		return result['latitude'], result['longitude'], result['firstBoroughName']
	except (KeyError, IndexError), e:
		print c
        	return None, None

def pelias(query):
	BASE = "http://pelias.mapzen.com/search?"
	params = {
		'input' : query,
		'zoom': 12,
		'bbox' : ''.join(str(e) for e in bounds)
	}
        url = BASE + urllib.urlencode(params)
        r, c = http.request(url)
        c = json.loads(c)
        try:
		result = c['features'][0]
		return result['geometry']['coordinates'][1],  result['geometry']['coordinates'][0], result['properties']['neighborhood']
	except:
		return None, None

