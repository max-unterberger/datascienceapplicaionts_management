from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from string import punctuation
from text_magic.functions import pipeline


with open(file="./quotes/quote_1_0.txt", mode="r", encoding="utf-8") as file:
    text = file.read()

words = pipeline(text).split(" ")

print(words)

