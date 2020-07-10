import requests
from bs4 import BeautifulSoup


def correct(file_name: str):
    with open(file_name, encoding='utf-8') as f:
        _list = f.readlines()
        _list = _list[2:-2]
    with open(file_name, 'w', encoding='utf-8') as f:
        for row in _list:
            print(row, file=f, end='')


def read(file_name: str):
    with open(file_name, encoding='utf-8') as f:
        for row in f:
            print(row, end='')


class Header(Exception):
    pass


class Navigable(Exception):
    pass


source = requests.get('https://www.omgubuntu.co.uk/2019/10/things-to-do-after-installing-ubuntu-19-10').text
soup, number = BeautifulSoup(source, 'lxml'), 0

with open('now.txt', 'w', encoding='utf-8') as file:

    for element in soup.find('div', class_='entry-content post-content'):
        if 'h3' in str(element):
            number = 1

        if 'div class="post-links"' in str(element):
            number = 0

        if number == 1:
            try:
                if 'h3' in str(element):
                    raise Header

                elif 'p class="wp-block-omg-buttons ta-center"' in str(element) \
                        or 'div class="wp-block-image"' in str(element) or 'figure class="wp-block' in str(element):
                    raise AttributeError

                elif 'bs4.element.NavigableString' in str(type(element)):
                    raise Navigable

                elif 'What else?' in str(element):
                    break

                else:
                    print(file=file)
                    print(str(element.text), file=file)

            except Header:
                print(f'\n\n*** {str(element.text)} ***', file=file)

            except (AttributeError, Navigable):
                pass

correct('now.txt')
read('now.txt')
