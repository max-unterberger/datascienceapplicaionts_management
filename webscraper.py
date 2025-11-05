from requests import get
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = get(url)

soup = BeautifulSoup(
    response.content,
    "html.parser"
)

quotes = soup.find_all(
    "div",
    attrs={"class": "quote"}
)

for index, quote in enumerate(quotes):
    print(index, quote.text)