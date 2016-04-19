#!/usr/bin/python

from geocoders import google
import csv
import os, sys
from collections import OrderedDict
from time import sleep


fieldnames = ['in_address','out_address','latlon']

outfile = open('output.csv','wb')
infile = sys.argv[1]

csvwriter = csv.DictWriter(outfile, fieldnames, dialect='excel')
csvwriter.writeheader() 

with open(infile, 'rU') as f:
	
	for line in f:
		line = line.encode('ascii', 'ignore').replace('\n','')
		results = google(line)
		try:
			dictresults = {
				'in_address':line.replace('"',''),'out_address':results[0].encode('ascii', 'ignore').replace('"',''), 'latlon':results[1]}
			print dictresults
		except:
			dictresults = {'in_address':line,'out_address':None, 'latlon':None }
			print "no results for " + line
		csvwriter.writerow(dictresults)
		sleep(1)
