Comparing Geocoders
===================

If you're thinking about moving off of Google Maps, by far the most difficult piece of the stack to replicate is its geocoder. Google probably has the most comprehensive database and by far the best address parsing. It also has this problematic line in its terms of service:

> Note: the Geocoding API may only be used in conjunction with a Google map; geocoding results without displaying them on a map is prohibited. For complete details on allowed usage, consult the [Maps API Terms of Service License Restrictions](http://code.google.com/apis/maps/terms.html#section_10_12).

So, no Google map, no Google geocoder.

We do have other options, of course:

 - [Yahoo Placefinder][y]
 - [Bing][b]
 - [Geocoder.us][g]
 - [Nominatum][n] (MapQuest)
 - [Pelias][p]

 [y]: http://developer.yahoo.com/geo/placefinder/
 [b]: http://msdn.microsoft.com/en-us/library/cc966793.aspx
 [g]: http://geocoder.us/
 [n]: http://wiki.openstreetmap.org/wiki/Nominatim
 [p]: http://pelias.mapzen.com/
 
To test these options against Google, I'm using a sample dataset that illustrates some of the known problems working with imperfect input. 

Every geocoding run will overwrite the results data in a file called `data/<geocoder>.csv` and log the result to `data/results.csv`.
