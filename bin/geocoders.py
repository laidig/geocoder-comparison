import httplib2
import json
import os
import urllib

from geopy.geocoders import GoogleV3, GeocoderDotUS, Bing

http = httplib2.Http()

def google(query):
    g = GoogleV3()
    try:
        place, (lat, lng) = g.geocode(query)
        return (lat, lng)
    except:
        return None, None

def geocoderdotus(query):
    us = GeocoderDotUS()
    try:
        place, (lat, lng) = us.geocode(query)
        return (lat, lng)
    except:
        return None, None

def bing(query):
	b = Bing( os.environ.get('BING_API_KEY'))
	try:
		place, (lat, lng) = b.geocode(query)
		return (lat, lng)
	except:
		return None, None

def yahoo(query):
    BASE = "http://where.yahooapis.com/geocode?"
    params = {
        'flags': 'JC', # JSON response, simplified
        'q': query,
        'appid': os.environ.get('YAHOO_APPLICATION_ID', '')
    }
    url = BASE + urllib.urlencode(params)
    r, c = http.request(url)
    c = json.loads(c)
    try:
        result = c['ResultSet']['Results'][0]
        return result['latitude'], result['longitude']
    except (KeyError, IndexError), e:
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
		return result['latitude'], result['longitude'], result['ntaName']
	except (KeyError, IndexError), e:
        	return None, None

def pelias(query):
	BASE = "http://pelias.mapzen.com/search?"
	params = {
		'input' : query,
		'zoom': 12,
		'bbox' : '40.4774,-74.2589,40.9176,-73.7004'
	}
        url = BASE + urllib.urlencode(params)
        r, c = http.request(url)
        c = json.loads(c)
        try:
		result = c['features'][0]
		return result['geometry']['coordinates'][1],  result['geometry']['coordinates'][0], result['properties']['neighborhood']
	except (KeyError, IndexError), e:
		return None, None

