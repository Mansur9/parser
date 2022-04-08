import requests
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup

from parsing.models import Network


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        for number_page in range(1, 25):
            self.process_page(number_page)
    
    def process_page(self, page_n):
        result = requests.get(f'https://www.retail.ru/rbc/tradingnetworks/?PAGEN_1={page_n}')
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
            name = item.find("div", {"class": "title"}).contents[0]
            #href_tags = item.find_all(href=True)
            link = item.find("a", {"class": "details"})["href"]
            #for link in item('a'):
            #    print(link.get('href'))
            Network.objects.update_or_create(name=name, defaults={"url": link})

