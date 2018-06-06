# -*- coding: utf-8 -*-

import unittest
from ..scraper.scraper import Scrapper
from urllib.error import URLError

class TestScraper(unittest.TestCase):
    def test_get_text_valid_url_wikipedia(self):
        url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
        scraper = Scrapper(url)
        txt = scraper.parse_xml()
        assert "Wikipedia" in txt and "enciclopedia" in txt and "libre" in txt

    def test_get_text_valid_url_nba(self):
        url = "https://www.nbamaniacs.com/"
        scraper = Scrapper(url)
        txt = scraper.parse_xml()
        assert "NOTICIAS" in txt and "RUMORES" in txt and "<p>" not in txt

    def test_get_xml_valid_url(self):
        url = "https://www.nbamaniacs.com/"
        scraper = Scrapper(url)
        xml = scraper.get_rss()
        assert "<a" in xml and "class" in xml and "NOTICIAS" in xml

    def test_get_xml_invalid_url(self):
        url = 123
        scraper = Scrapper(url)
        self.assertRaises(URLError, scraper.get_rss)

    def test_get_xml_unexistent_url(self):
        url = "https://www.auhfaiguisgfa.com"
        scraper = Scrapper(url)
        self.assertRaises(URLError, scraper.get_rss)

    def test_get_xml_invalid_decodification_in_url(self):
        url = "https://www.google.es/"
        scraper = Scrapper(url)
        self.assertRaises(URLError, scraper.get_rss)

    def test_get_xml_invalid_access_url(self):
        url = "https://www.plusdede.com/"
        scraper = Scrapper(url)
        self.assertRaises(URLError, scraper.get_rss)

if __name__ == '__main__':
    unittest.main()
