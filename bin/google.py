#!/usr/bin/python

from geocoders import google
import csv
import os, sys
from collections import OrderedDict
from time import sleep


fieldnames = ['in_address','out_address','latlon']

outfile = open('output.csv','wb')
infile = sys.argv[1]

csvwriter = csv.DictWriter(outfile, fieldnames)
csvwriter.writeheader() 

with open(infile, 'rU') as f:
	
	for line in f:
		line = line.encode('ascii', 'ignore')
		results = google(line)
		print results
		try:
			dictresults = {'in_address':line,'out_address':results[0].encode('ascii', 'ignore'), 'latlon':results[1]}
			print dictresults
		except:
			dictresults = {'in_address':line,'out_address':None, 'lat':None , 'lon':None}
			print "no results for " + line
		csvwriter.writerow(dictresults)
		sleep(1)
