from typing import Dict
from bs4 import BeautifulSoup
import requests
import re

URL = "https://www.johnlewis.com/2018-apple-ipad-pro-12-9-inch-a12x-bionic-ios-wi-fi-cellular-512gb/space-grey/p3834614"
TAG_NAME = "p"
QUERY = {"class": "price price--large"}

request = requests.get(URL)
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find(TAG_NAME, QUERY)
string_price = element.text.strip()

pattern = re.compile(r"(\d+,?\d+\.\d+)")
match = pattern.search(string_price)
found_price = match.group(1)
without_commas = found_price.replace(",", "")
price = float(without_commas)

print(price)
