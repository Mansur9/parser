import requests
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup

from parsing.models import Network


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        result = requests.get('https://www.retail.ru/rbc/tradingnetworks/')
        print(f"result code is {result.status_code}")
        if result.status_code == 200:
            print('Success!  == 200')
        elif result.status_code == 400:
            print('400')
        # print(result.headers)
        # print(result.text)

        soup = BeautifulSoup(result.text, 'html.parser')
        for item in soup.find("div", {"class": "events__row"}).findAll("div", {"class": "col"}):
            print(item.find("div", {"class": "title"}))
            print(item.find("div", {"class": "title"}).contents[0])
            #href_tags = item.find_all(href=True)
            print(item.find("a", {"class": "details"})["href"])
            #for link in item('a'):
            #    print(link.get('href'))
            

