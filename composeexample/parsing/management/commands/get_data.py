import requests
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup

from parsing.models import Network


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        for network in Network.objects.filter(id__in=[465, 466]):
            print(network.name)
            n_name = network.name
            Network.objects.update_or_create(description=n_name)
