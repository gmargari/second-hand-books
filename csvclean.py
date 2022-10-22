#!/bin/env python
# coding=utf8
import csv
import re
import sys
import unicodedata


def strip_accents(s):
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


REPLACEMENTS = (
    ("(μεταχειρισμένο|μεταχειρισμενο)", ""),
    ("\s+", " "),
)


def strclean(s):
    for old, new in REPLACEMENTS:
        s = re.sub(old, new, s, flags=re.IGNORECASE)
    return strip_accents(s).strip()


if len(sys.argv) != 3:
    print(f"Syntax: {sys.argv[0]} INFILE.csv OUTFILE.csv")
    sys.exit(1)
infile = sys.argv[1]
outfile = sys.argv[2]

# row: 0: title, 1: author, 2: price, 3: normal_price, 4: url
row_sort = lambda row: (
    strclean(row[0].lower()),
    strclean(row[1].lower()),
    row[4].lower(),
)

reader = csv.reader(open(infile, encoding="utf8"))
header = next(reader)
unique_rows = set(tuple(x) for x in reader)
sorted_rows = [
    (strclean(title), strclean(author), price, normal_price, f'<a href="{url}">{url}</a>')
    for title, author, price, normal_price, url in sorted(unique_rows, key=row_sort)
]

csv.writer(open(outfile, "w", encoding="utf8", newline="")).writerows(
    [header] + sorted_rows
)
