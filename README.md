# second-hand-books
Scrape greek sites for second hand books.

# Install
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: source venv/Scripts/activate
pip install scrapy csvtotable
```

# Run
```bash
scrapy runspider protoporia.py
```
A file `protoporia.csv` will be created.

# Visualize

```bash
# clean up .csv a bit
./csvclean.py protoporia.csv protoporia.clean.csv

# convert csv to html
csvtotable -o protoporia.clean.csv protoporia.html

# open protoporia.html
```
