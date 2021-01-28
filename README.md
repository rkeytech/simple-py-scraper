# PY Scraper

A simple Python scraper for web pages. It uses BeautifulSoup to scrape data from a simple website and stores them into a database.

---

## Description

A Python web scraper made with the `BeautifulSoup` module. Its work is pretty simple. The user configures the settings in his own needs, for example the page he wants to scrape or what elements, and runs the program. It is as much modular as it can be, meaning that you can choose what elements you want to find, the path of the element, the type you want to retrieve, and other features I will add later on. When the scraper ends, it stores the results in a SQLite Database for further use.

## Python Modules

- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)
- [SQLite](https://sqlite.org/index.html)
- [Requests](https://2.python-requests.org/en/master/)
- [ConfigParser](https://docs.python.org/3.8/library/configparser.html)
- [ArgParser](https://docs.python.org/3.8/library/argparse.html)
