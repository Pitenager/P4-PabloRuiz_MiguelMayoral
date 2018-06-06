# -*- coding: utf-8 -*-
from django.shortcuts import render
from .text_analyzer.text_analyzer import *
from .models import Word
from django.utils import timezone
from .forms import IndexForm
import time

def get_text(request):
    if request.method == 'POST':

        form = IndexForm(request.POST)
        form2 = IndexForm()

        if form.is_valid():
            my_text = "https://www.theguardian.com/international/rss"
            my_date = form.cleaned_data['my_date']
            if (my_date == ''):
                my_date = time.strftime('%Y-%m-%d')
                words = Word.objects.filter(insert_date__contains=my_date).order_by('-apariciones')
                if not words:
                    text_analyzed = TextAnalyzer.run(my_text)
                    i = 1
                    print(text_analyzed)
                    for palabra in text_analyzed:
                        Word.objects.create(word=palabra[0], apariciones=palabra[1])
                        word = Word.objects.get(id=i)
                        word.publish()
                        i = i + 1
                    words = Word.objects.order_by('-apariciones')
                return render(request, 'index.html', {'form': form2,'words': words})
            else:
                words = Word.objects.filter(insert_date__contains=my_date).order_by('-apariciones')
                if not words and my_date != time.strftime('%Y-%m-%d'):
                    words = ["There is no data for the day required"]
                elif not words and my_date == time.strftime('%Y-%m-%d'):
                    text_analyzed = TextAnalyzer.run(my_text)
                    i = 1
                    print(text_analyzed)
                    for palabra in text_analyzed:
                        Word.objects.create(word=palabra[0], apariciones=palabra[1])
                        word = Word.objects.get(id=i)
                        word.publish()
                        i = i + 1
                    words = Word.objects.order_by('-apariciones')
                return render(request, 'index.html', {'form': form2,'words': words})

    else:
        form = IndexForm()

    return render(request, 'index.html',{'form':form})