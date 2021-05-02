import requests
from bs4 import BeautifulSoup
import time

print("Before starting please make sure that you have an active internet connection and enter a valid name when asked.")
time.sleep(3)
user_input = input('What do you want to search on Wikipedia?:')
link = "https://en.wikipedia.org/wiki/" + user_input


def download_data(url):
    response = requests.get(url)
    plain_text = response.text
    soup = BeautifulSoup(plain_text, features='lxml')
    print(soup.find_all('p')[0].get_text())
    print(soup.find_all('p')[1].get_text())


download_data(link)
