# Парсим онлайн-библиотеку и создаем сайт со скачанными книгами

Парсинг он-лайн библиотеки https://tululu.org/,
(книги жанра **Научная фантастика**) и создание нового сайта, 
где книги доступны для скачивания локально. 


## Запуск

Для запуска у вас уже должен быть установлен Python 3.

- Скачайте код
- Установите зависимости командой

```pip install -r requirements.txt```
- Запустите командой 

```python3 parse_website.py```

## Описание проекта
Проект позволяет для книг жанра **Научная фантастика** из онлайн-библиотеки:
- выгрузить `json` файл содержащий Название, Автора, Жанр(ы),
Комментарии
- выгрузить обложку
- выгрузить саму книгу в формате `.txt`
- книги можно выгрузить с одной или нескольких страниц сайта

### Задание страниц с которых будут выгружаться книги

Страницы с которых требуется выгрузить книги задается 
начальным (`--start_page`) и конечным (`--end_page`) номером страницы, например, 
команда ниже выгрузит книги со страниц  
с 20 по 40

```python main.py -s 20 -e 40```

При запуске без параметров по умолчанию будут выгружены книги 
со страницы 1

### Прочие параметры

- Параметр `--dest_folder` задает каталог в который будут выгружены данные. Если 
каталог не задан то данные выгружаются в каталог _folder_
Например, такая команда выгрузит данные в каталог _new_:

```python main.py -df /new```

- Параметр `--skip_txt` указывает парсеру выгружать или нет текст книг. 
Например, если не требуется выгружать текст, то это можно сделать такой командой:

```python main.py -txt```

- Параметр `--skip_img` указывает парсеру выгружать или нет обложки книг. 
Например, если не требуется выгружать обложки, то это можно сделать такой командой:

```python main.py -img```


Для запуска скрипта, который создает многстраничнфый сайт 
с загруженныыми книгами запустите команду:

```python3 render_website.py```

Команда создает в корневом каталоге каталог `pages`, в котором 
формирует страницы сайта.

На каждой карточке книги отображаются:
- название
- автор
- обложка (если есть)
- жанр(ы)
- ссылка для скачивания текста книги


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
