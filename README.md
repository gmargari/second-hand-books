# second-hand-books
Scrape greek sites for second hand books

# Install
```
python3 -m venv venv
source venv/bin/activate 
pip install scrapy
```

# Run
```
scrapy runspider <spider-name.py>
```
A file `<spider-name.csv>` will be created.

You can then create new [Google Sheet](https://docs.google.com/spreadsheets/u/0/create), `File` -> `Import`, select the .csv, and you're ready to go!
