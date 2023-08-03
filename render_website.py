import itertools
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import argparse
import os
# import dotenv
from more_itertools import chunked



def books(books):
    with open(books, "r", encoding="utf-8") as my_file:
        books_json = my_file.read()

    books = json.loads(books_json)
    # print(books)
    return(books)


def main():
    # print(os.sep)
    parser = argparse.ArgumentParser(description="Путь к файлу, содержащему базу данных для сайта")
    parser.add_argument('--path', help='Путь к файлу', default='books/books_json')
    args = parser.parse_args()
    books_path = args.path

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    cards_by_two = list(chunked(books(books_path), 2))

    print(cards_by_two)

    # for card in cards_by_two:
    #     print(card)
    #     print()

    rendered_page = template.render(
        cards_divided=cards_by_two,
        # book_cards=books(books_path),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()