#!/usr/bin/env python
"""
Bulk geocode a set of addresses, outputting a csv.
This script is meant to test various geocoders. Data will be
overwritten on each run.
"""
import argparse
import csv
from geocoders import *
import os, sys
from collections import OrderedDict

infile = sys.argv[1]

def multi_geocode(q):
	gc_dict = OrderedDict([
		('google', google(q)),
		('mapquest', mapquest(q)),
		('nycgeoclient', nycgeoclient(q)),
		('pelias', pelias(q)),
		('bing', bing(q))
	])
	return gc_dict
#print multi_geocode('2 broadway NYC')

fieldnames = ['google','mapquest','nycgeoclient','pelias','bing']

outfile = open('out.csv','wb')
csvwriter = csv.DictWriter(outfile, fieldnames)
csvwriter.writeheader()

with open(infile, 'rU') as f:
	for line in f:
		results = multi_geocode(line)
		csvwriter.writerow(results)
		

