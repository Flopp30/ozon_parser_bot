import requests
from bs4 import BeautifulSoup

from ozon_parser.settings import PARSER_LINK, MAX_ITEMS_PARSED_COUNT, DEFAULT_ITEMS_PARSED_COUNT

def main():
    print(PARSER_LINK)
    print(MAX_ITEMS_PARSED_COUNT)
    print(DEFAULT_ITEMS_PARSED_COUNT)


if __name__ == "__main__":
    main()
