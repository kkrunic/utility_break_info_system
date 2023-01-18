from bs4 import BeautifulSoup
import requests 

class ShutdownScrapper():
    def __init__(self) -> None:
        self.base_url = None
        self.response = None
        self.soup = None
        self.date = None
        self.headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }   