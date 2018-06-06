# -*- coding: utf-8 -*-

import unittest
from ..text_analyzer.text_analyzer import TextAnalyzer

class TestTextAnalyzer(unittest.TestCase):
    def test_string_lower_string_capitalized(self):
        analyzer = TextAnalyzer()
        text = "asd ASD"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd","asd"]

    def test_semi_capitalized_strings(self):
        analyzer = TextAnalyzer()
        text = "Asd AsD"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd","asd"]

    def test_symbol_doc(self):
        analyzer = TextAnalyzer()
        text = "asd. Asd"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd","asd"]

    def test_symbol_coma(self):
        analyzer = TextAnalyzer()
        text = "asd,"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd"]

    def test_symbol_doc_and_coma(self):
        analyzer = TextAnalyzer()
        text = "asd; Asd"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd","asd"]

    def test_symbol_double_points(self):
        analyzer = TextAnalyzer()
        text = "asd: Asd"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd","asd"]

    def test_symbol_slash(self):
        analyzer = TextAnalyzer()
        text = "asd/ Asd"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd", "asd"]

    def test_symbol_dollar(self):
        analyzer = TextAnalyzer()
        text = "asd$ Asd"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd","asd"]

    def test_symbol_arroba(self):
        analyzer = TextAnalyzer()
        text = "asd@ Asd"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd","asd"]

    def test_symbol_almohadilla(self):
        analyzer = TextAnalyzer()
        text = "asd# Asd"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd","asd"]

    def test_string_stopword_string(self):
        analyzer = TextAnalyzer()
        text = "asd upon asd"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd","asd"]

    def test_symbol_bar(self):
        analyzer = TextAnalyzer()
        text = "asd- Asd"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd","asd"]

    def test_symbol_low_bar(self):
        analyzer = TextAnalyzer()
        text = "asd_ Asd"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd","asd"]

    def test_symbol_upper_interrogation(self):
        analyzer = TextAnalyzer()
        text = "asd? Asd"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd","asd"]

    def test_symbol_upper_exclamation(self):
        analyzer = TextAnalyzer()
        text = "asd! Asd"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd","asd"]

    def test_symbol_percentage(self):
        analyzer = TextAnalyzer()
        text = "asd% Asd"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd","asd"]

    def test_symbol_parenthesis(self):
        analyzer = TextAnalyzer()
        text = "asd() Asd"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd","asd"]

    def test_symbol_numbers(self):
        analyzer = TextAnalyzer()
        text = "asd 1234asd"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asd","asd"]

    def test_symbol_numbers_between_letters(self):
        analyzer = TextAnalyzer()
        text = "as1d2As3d"
        text = TextAnalyzer.prepare_text(analyzer,text)
        assert text == ["asdasd"]

    def test_sort_dictionary(self):
        analyzer = TextAnalyzer()
        analyzer.palabras_leidas = {"a":1,"b":3,"c":2}
        analyzer.palabras_leidas = TextAnalyzer.sortDict(analyzer)
        res = [("b",3),("c",2),("a",1)]
        assert analyzer.palabras_leidas == res

    def test_sort_dictionary_tie_words(self):
        analyzer = TextAnalyzer()
        analyzer.palabras_leidas = {"a": 3, "b": 3, "c": 2}
        analyzer.palabras_leidas = TextAnalyzer.sortDict(analyzer)
        res = [("b", 3), ("a", 3), ("c", 2)]
        assert analyzer.palabras_leidas == res

    def test_analyze(self):
        analyzer = TextAnalyzer()
        text = ["hola","hola","hola","adios"]
        TextAnalyzer.analyze(analyzer,text)
        assert analyzer.palabras_leidas['hola']==3 and analyzer.palabras_leidas['adios']==1


if __name__ == '__main__':
    unittest.main()
