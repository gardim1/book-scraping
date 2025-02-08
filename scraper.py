import requests
from bs4 import BeautifulSoup

def scrape_books():
    url = "http://books.toscrape.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Erro ao acessar a página:", e)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")
    if not books:
        print("Nenhum livro encontrado na página.")
        return

    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text
        print("Titulo:", title)
        print("Preco:", price)
        print("-" * 30)

if __name__ == "__main__":
    scrape_books()
