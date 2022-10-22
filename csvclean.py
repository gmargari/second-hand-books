#!/bin/env python
#coding=utf8
import csv
import re
import sys
import unicodedata

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

if len(sys.argv) != 3:
	print(f'Syntax: {sys.argv[0]} INFILE.csv OUTFILE.csv')
	sys.exit(1)

infile = sys.argv[1]
outfile = sys.argv[2]

strclean = lambda s: re.sub(u'(μεταχειρισμένο|μεταχειρισμενο)', '', s, flags=re.IGNORECASE).strip()
row_sort = lambda row: (strip_accents(row[1].lower()), strip_accents(row[0].lower()), row[4].lower())

reader = csv.reader(open(infile, encoding='utf8'))
header = next(reader)
unique_rows = set(tuple(x) for x in reader)
sorted_rows = [(strclean(title), author, price, normal_price, url) for title, author, price, normal_price, url in sorted(unique_rows, key=row_sort)]

csv.writer(open(outfile, 'w', encoding='utf8', newline='')).writerows([header] + sorted_rows) 
