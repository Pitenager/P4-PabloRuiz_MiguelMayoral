# -*- coding: utf-8 -*-

import os
from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
from ..scraper.scraper import Scrapper
import operator


#http://websitetips.com/articles/copy/lorem/ipsum.txt

class TextAnalyzer(object):
    """A class to analyze a text"""

    def __init__(self):
        self.palabras_leidas = {}
        self.stopwords = [" about "," above "," after "," among "," at "," before "," behind "," below "," beneath "," beside "," between "," but "," by "," down "," except "
                         ," for "," from "," in "," into "," like "," near "," of "," off "," on "," over "," since "," through "," throughout "," till "," until "," to "," under ",
                         " up "," upon "," with "," without "," across "," also "," anyone "," anything "," back "," bill "," both "," could "," can't "," cannot "," down ",
                          " due "," during "," either "," ever "," every "," few "," for "," former "," has "," hence "," hereby "," inc "," if "," it "," its "," latter ",
                          " less "," ltd "," many "," may "," might "," mill "," namely "," never "," nevertheless "," nobody "," noone "," often "," once "," only "," onto ",
                          " other "," others "," otherwise "," our "," ours "," ourselves "," own "," perhaps "," please "," per "," rather "," same "," several "," should ",
                          " some "," something "," somewhere "," sometimes "," somehow "," someone "," sometime "," still "," such "," than "," that "," the "," them "," then ",
                          " there "," their "," thereafter "," therefore "," thereby "," therein "," thereupon "," these "," those "," to "," too "," together "," towards ",
                          " towards "," under "," until "," very "," via "," well "," were "," what "," whatever "," when "," who "," whenever "," where "," whereby "," whereafter ",
                          " wherein "," wherever "," which "," while "," whom "," why "," will "," with "," within "," without "," yet "," yourself "," yourselves "]

        self.symbols = ["-","–","_","?","!","’","'",'“','”',"‘","0","1","2","3","4","5","6","7","8","9","0","/","$",".",",",";",":","%","(",")","{","}","[","]",">","<","\n",
                        "@", "#","+","&","~","\r"]

    @staticmethod
    def prepare_text (self, text):
        text = text.replace("\n", "")
        text = text.lower()

        for line in self.stopwords:
            text = text.replace(line," ")

        text = text.replace("\r", " ")

        for symbol in self.symbols:
            text = text.replace(symbol,"")

        text = text.split(" ")

        return text

    @staticmethod
    def analyze (self,text):
        for i in text:
            claves = self.palabras_leidas.keys()
            if i == "":
                continue
            elif i not in claves:
                self.palabras_leidas[i]=1
            else:
                valor = self.palabras_leidas[i]
                valor = valor +1
                self.palabras_leidas[i] = valor


    @staticmethod
    def sortDict(self):
        self.palabras_leidas = sorted(self.palabras_leidas.items(), key=operator.itemgetter(1))
        self.palabras_leidas.reverse()

        return self.palabras_leidas

    @staticmethod
    def printResult(self):
        tamaño = len(self.palabras_leidas)

        for clave in range(tamaño):
            print(self.palabras_leidas[clave][0]+": ",self.palabras_leidas[clave][1])

    @staticmethod
    def get_text(url):
        if type(url)!= str:
            raise URLError("La URL no es válida")
        else:
            try:
                response = urlopen(url)
            except:
                raise URLError("La URL no existe")
            full_text = response.read().decode("utf-8")
            return full_text

    @staticmethod
    def run(url):
        analyzer = TextAnalyzer()
        scraper = Scrapper(url)
        txt = scraper.parse_xml()
        #text = analyzer.get_text(url)
        text = analyzer.prepare_text(analyzer,str(txt))
        analyzer.analyze(analyzer,text)
        return analyzer.sortDict(analyzer)
        #analyzer.printResult(analyzer)