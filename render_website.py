from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import argparse
import json
import os
from more_itertools import chunked



def books(books_path):
    with open(books_path, "r", encoding="utf-8") as my_file:
        books_json = my_file.read()

    books = json.loads(books_json)
    return(books)


def main():
    parser = argparse.ArgumentParser(description="Путь к файлу, содержащему базу данных для сайта")
    parser.add_argument('--path', help='Путь к файлу', default='books/books_json')
    args = parser.parse_args()
    books_path = args.path

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    os.makedirs('pages')

    pages = list(chunked(books(books_path), 20))
    for index, book in enumerate (pages):

        divided_by_columns = list(chunked(book, 2))
        rendered_page = template.render(
            book_cards=divided_by_columns,
            pages=len(pages),
            current_page=index+1
        )

        with open(os.path.join('pages', f'index{index+1}.html'), 'w', encoding="utf8") as file:
            file.write(rendered_page)


    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()