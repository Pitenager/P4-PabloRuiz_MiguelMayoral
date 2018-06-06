# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
import re

class Scrapper:

    def __init__(self, url):
        self.url = url
        self.list_of_titles = []
        self.list_of_text = []
        self.xml = []

    def parse_xml(self):
        self.xml = self.get_rss()
        soup = BeautifulSoup(self.xml,'html.parser')
        text = soup.get_text()
        text = text.replace("<p>", " ")
        text = text.replace("href", " ")
        text = text.replace('"', " ")
        text = text.replace("=", " ")
        text = text.replace("</p>", " ")
        text = text.replace("<a", " ")
        text = text.replace("</a>", " ")
        text = text.replace("<ul", " ")
        text = text.replace("<li", " ")
        text = text.replace("</ul>", " ")
        text = text.replace("</li>", " ")
        text = text.replace("<em>", " ")
        text = text.replace("</em>", " ")
        text = text.replace(">", " ")
        text = re.sub(r"http\S+", "", text)
        return text

    def get_rss(self):
        try:
            return urlopen(self.url).read().decode('utf-8')
        except:
            raise URLError("La URL no es válida")

