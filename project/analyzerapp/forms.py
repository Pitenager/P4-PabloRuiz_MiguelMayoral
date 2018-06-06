# -*- coding: utf-8 -*-

from django import forms

class IndexForm(forms.Form):
    my_text = "https://www.theguardian.com/international/rss"
    my_date = forms.CharField(label="Insert optional date to filter (yyyy-mm-dd)",max_length=10,required=False)