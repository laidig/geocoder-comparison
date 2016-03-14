#!/usr/bin/env python
"""
Bulk geocode a set of addresses, outputting a csv.
This script is meant to test various geocoders. Data will be
overwritten on each run.
"""
import argparse
import csv
import string
from geocoders import *
import os, sys
from collections import OrderedDict

infile = sys.argv[1]

def multi_geocode(q):
	q = string.lower(q)
	q = q.replace('\n','')
	q = q.replace('at','and')
	q = q.replace('/','and')
	q = q.replace('&','and')
	gc_dict = OrderedDict([
		('address',q),
		('google', google(q)),
		('nycgeoclient', nycgeoclient(q)),
		('pelias', pelias(q)),
		('bing', bing(q))
	])
	return gc_dict

fieldnames = ['address','google','nycgeoclient','pelias','bing']

outfile = open('out.csv','wb')
csvwriter = csv.DictWriter(outfile, fieldnames)
csvwriter.writeheader()

with open(infile, 'rU') as f:
	for line in f:
		results = multi_geocode(line)
		print results
		csvwriter.writerow(results)
		

