"""
production text summarizer for wikipedia articles using gensim and summa algorithms
"""
import toga
import bs4 as bs
import urllib.request
import re
import nltk
nltk.download("punkt")
nltk.download("stopwords")
from nltk import word_tokenize, sent_tokenize
import heapq
import logging
from summarizer.functions import scraped_data
logging.basicConfig(format = '%(asctime)sw : %(levelname)s : %(message)s', level = logging.INFO)
from gensim.summarization import summarize
from gensim.summarization import keywords
from summa import summarizer
from summa import keywords



from toga.style import Pack
from toga.style.pack import *


class TextSummarizer(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        
        #Box definition
        main_box = toga.Box()
        Title_box = toga.Box()
        Intro_box = toga.Box()
        Url_box = toga.Box()
        length_box = toga.Box()
        return_box = toga.Box()
        button_box = toga.Box()
        
        
        #Label definition
        Title_label = toga.Label('Welcome to the Text Summarizer app !', style = Pack(text_align = CENTER))
        Intro_label = toga.Label('This application allows you to summarize any text inputs through the use of two extractive summarizers', style = Pack(text_align = CENTER))
        Url_label = toga.Label('URL : ')
        length_label = toga.Label('Size of the summary :')
        return_label = toga.Label('text summary : ')


        #Text input
        Url_link = toga.TextInput()
        self.url = Url_link.value
        length_value = toga.TextInput()
        f_summary = toga.TextInput(readonly = True)
        
        def gensim_function(widget):
            text_input = scraped_data(Url_link.value)
            text_size = float(length_value.value)
            gen_sum = summarize(text_input,ratio=text_size)
            f_summary.value = gen_sum
            return
            
        def summa_function(widget):
            text_input = scraped_data(Url_link.value)
            text_size = float(length_value.value)
            gen_sum = summarizer.summarize(text_input,ratio=text_size)
            f_summary.value = gen_sum
            return
     
        #Button
        button_gen = toga.Button('gensim summarizer', on_press = gensim_function)
        button_summa = toga.Button('summa summarizer', on_press = summa_function)


        #main Box architecture
        Title_box.add(Title_label)
        Intro_box.add(Intro_label)
        Url_box.add(Url_label)
        Url_box.add(Url_link)
        length_box.add(length_label)
        length_box.add(length_value)
        button_box.add(button_gen)
        button_box.add(button_summa)
        return_box.add(return_label)


        #return_box.add(f_summary)
        main_box.add(Title_box)
        main_box.add(Intro_box)
        main_box.add(toga.Divider())
        main_box.add(Url_box)
        main_box.add(length_box)
        main_box.add(button_box)
        main_box.add(toga.Divider())
        main_box.add(f_summary)
        

        #style boxes
        main_box.style.update(direction = COLUMN, padding = 20)
        Intro_box.style.update(direction = ROW, padding = 15)
        Url_box.style.update(direction = ROW, padding_top = 15)
        length_box.style.update(direction = ROW, padding = 15, padding_left = 0)
        button_box.style.update(direction = ROW, padding = 15)
        #return_box.style.update(direction = COLUMN, padding_top = 15)
        
        
        #style sub elements
        Title_label.style.update(flex = 1)
        Intro_label.style.update(flex = 1)
        Url_link.style.update(padding_left = 10, width = 550)
        Url_label.style.update(text_align = LEFT)
        length_value.style.update(padding_left = 10, width = 60)
        return_label.style.update(flex = 1, text_align = CENTER)
        button_gen.style.update(padding_left = 100)
        button_summa.style.update( padding_left = 80)
        f_summary.style.update(flex = 1, height = 400)
        

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return TextSummarizer()
