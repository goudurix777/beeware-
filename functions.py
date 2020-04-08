"""
production text summarizer functions for wikipedia articles using gensim and summa algorithms
"""
import bs4 as bs
import urllib.request
import re
import nltk
nltk.download("punkt")
nltk.download("stopwords")
from nltk import word_tokenize, sent_tokenize
import heapq
import logging
logging.basicConfig(format = '%(asctime)sw : %(levelname)s : %(message)s', level = logging.INFO)

def scraped_data(url_topull):
    scraped_data = urllib.request.urlopen(url_topull)
    article = scraped_data.read()
    parsed_article = bs.BeautifulSoup(article,'html')
    paragraphs = parsed_article.find_all('p')
    article_text = ""
    for p in paragraphs:
        article_text += p.text
    text = article_text
    print("Data pull done")
    return text

