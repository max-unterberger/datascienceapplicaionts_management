from requests import get
from bs4 import BeautifulSoup
from time import sleep

base_url = " https://quotes.toscrape.com/page/"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"

for page in range(1, 10):

    # Eigentliche Seiten URL zusammenbauen
    url = base_url + str(page)
    print(url)

    # Seite abfragen
    response = get(url, headers={"User-Agent": user_agent})

    # Suchkartei erzeugen
    soup = BeautifulSoup(
        response.content,
        "html.parser"
    )

    # Alle Zitate-Boxen im HTML finden
    quotes = soup.find_all("div", attrs={"class": "quote"})

    # Über Ergebnisliste iterieren
    for index, quote in enumerate(quotes):

        # Eigentliches Zitat finden
        statement = quote.find_next("span", attrs={"class": "text"})

        # Zitat in Quotes-Ordner speichern
        with open(f"quotes/quote_{page}_{index}.txt", "w", encoding="utf-8") as file:
            file.write(statement.text)

