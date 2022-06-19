#!/bin/env python
#coding=utf8
import csv
import re
import sys

if len(sys.argv) != 3:
	print(f'Syntax: {sys.argv[0]} INFILE.csv OUTFILE.csv')
	sys.exit(1)

infile = sys.argv[1]
outfile = sys.argv[2]

strclean = lambda s: re.sub(u'(μεταχειρισμένο|μεταχειρισμενο)', '', s, flags=re.IGNORECASE).strip()

reader = csv.reader(open(infile))
header = next(reader)
sorted_rows = [(strclean(title), author, price, normal_price, url) for title, author, price, normal_price, url in sorted(reader, key=lambda row: (row[1].lower(), row[0].lower()))]

csv.writer(open(outfile, 'w')).writerows([header] + sorted_rows) 
