from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
import urllib3

def parse():
    urllib3.disable_warnings()
    url = 'https://omgtu.ru/general_information/faculties/' # передаем необходимы URL адрес
    page = requests.get(url, verify=False) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('ul', class_='') # находим  контейнер с нужным классом
    description = ''
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('li'): # находим тег <li>
            description = data.text # записываем в переменную содержание тега

    print(description)