A small tool to scrap www.realclearpolitics.com/ poll datas

Installing
==========

Dependencies
-------------------
The scraper depends on scrapy and python-twisted. Make sure they are installed on your machine before starting.

## Ubuntu

```sh
pip install scrapy
sudo apt-get install python-twisted
```


Usage
==========

Use the scraper.py script.

The `--noavg` option excludes the RCP Average.

```sh
python scraper.py [--noavg] url [output.csv]
```

Example :

```sh
python scraper.py http://www.realclearpolitics.com/epolls/2016/president/us/2016_democratic_presidential_nomination-3824.html national.csv
```

