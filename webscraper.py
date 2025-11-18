from requests import get
from bs4 import BeautifulSoup

for page in range(1, 10):
    url = "https://quotes.toscrape.com/" + f"page/{page}/" 

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
        with open(f"./quotes/quote_{index}.txt","a") as file: 
            file.write(f"{index} {quote.text}")
        print(index, quote.text)