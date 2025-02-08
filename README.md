##Web Scraping com Python - Exemplo de Extração de Livros

Este repositório contém dois exemplos de web scraping em Python que utilizam as bibliotecas requests e BeautifulSoup para extrair informações do site "Books to Scrape" (http://books.toscrape.com/).

Descrição dos Arquivos:

scraper.py
Código simples que realiza web scraping da página inicial do site, extraindo e exibindo o título e o preço de todos os livros encontrados.
scraper-with-filter.py
Código similar ao scraper.py, porém com uma modificação para filtrar e exibir somente os livros com preço menor que 30. Esse script utiliza expressões regulares para limpar a string do preço antes de convertê-la para número.
Pré-requisitos:

Python 3.x
Dependências: Para executar os scripts, é necessário instalar as seguintes bibliotecas: • requests (https://pypi.org/project/requests/) • beautifulsoup4 (https://pypi.org/project/beautifulsoup4/)

Você pode instalá-las utilizando o pip: pip install requests beautifulsoup4

Como Executar:

Código Simples (scraper.py): Este script realiza o scraping da página e exibe todos os livros encontrados. Para executá-lo, utilize o comando: python scraper.py

Código com Filtro (scraper-with-filter.py): Este script realiza o scraping, converte os preços para números (utilizando expressões regulares para limpar a string do preço) e exibe somente os livros com preço menor que 30. Para executá-lo, utilize o comando: python scraper-with-filter.py

Explicação dos Códigos:

scraper.py:

Requisição HTTP:
O script envia uma requisição GET para http://books.toscrape.com/ utilizando a biblioteca requests.
Processamento do HTML:
O HTML retornado é processado com o BeautifulSoup para extrair os elementos de livros (tags <article> com a classe "product_pod").
Extração de Dados:
Para cada livro, o título (extraído do atributo "title" da tag <a>) e o preço (conteúdo da tag <p> com a classe "price_color") são extraídos e exibidos no console.
scraper-with-filter.py:

Requisição e Processamento:
Assim como no scraper.py, o script realiza uma requisição e processa o HTML com o BeautifulSoup.
Limpeza do Preço:
Utiliza o módulo re (expressões regulares) para remover todos os caracteres indesejados da string do preço, deixando apenas dígitos e o ponto decimal.
Conversão e Filtro por Preço:
Após limpar a string, o script converte o valor para float e verifica se o preço é menor que 30. Se for, o livro é adicionado à lista de livros filtrados.
Exibição dos Resultados:
Ao final, os livros que atendem ao critério de preço são exibidos no console.
Observações:
O site utilizado tem como objetivo estudar sobre webscraping.
