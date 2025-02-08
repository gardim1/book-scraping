import requests
from bs4 import BeautifulSoup
import re 

def scrape_books():
    url = "http://books.toscrape.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Erro ao acessar a pagina ", e)
        return

    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    
    livros_filtrados = []

    for book in books:
        title = book.find("h3").find("a")["title"]
        price_text = book.find("p", class_="price_color").text.strip()
        
        price_numbers = re.sub(r'[^0-9.]', '', price_text)
        
        try:
            price_value = float(price_numbers)
        except ValueError:
            print(f"Nao foi possível converter o preco {price_text} para numero.")
            continue

        if price_value < 30:
            livros_filtrados.append((title, price_text))

    if livros_filtrados:
        print("Livros com preco menor que 30:")
        for title, price in livros_filtrados:
            print("Titulo:", title)
            print("Preco:", price)
            print("-" * 30)
    else:
        print("Nenhum livro com preco menor que 30 foi encontrado :((")

if __name__ == "__main__":
    scrape_books()
