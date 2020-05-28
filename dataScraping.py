import csv
import os
from newspaper import Article
import nltk
nltk.download('punkt')
import string
import re

sections = ["http://www.haber7.com/guncel/p"]

pages = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
         21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
kelimesay = 0

with open('C:/Users/asus/PycharmProjects/webScraping/veriler/data.csv', 'a', encoding='utf-8', newline='') as f_output:
    csv_print = csv.writer(f_output)

    csv_print.writerow(['url', 'segment_no', 'cumle_icerigi', 'sözcük_sayisi'])

    for page in pages:
        url ="http://www.haber7.com/guncel/p" + str(page)
        i = 0
        article_name = Article(url,language="tr")
        article_name.download()
        article_name.parse()
        article_name.nlp()

        print("Url: \n" + article_name.url)

        tokenized_text = article_name.text

        tokenized_text = re.sub(r"\[\d+\]"," ",tokenized_text)
        tokenized_text = re.sub(r"\["," ",tokenized_text)
        tokenized_text = re.sub(r"\]"," ",tokenized_text)
        tokenized_text = re.sub(r"\("," ",tokenized_text)
        tokenized_text = re.sub(r"\)"," ",tokenized_text)
        tokenized_text = re.sub(r"[:,'\"-]"," ",tokenized_text)
        tokenized_text = re.sub(r"\s+"," ",tokenized_text)
        tokenized_text = tokenized_text.strip()


        sentences = nltk.sent_tokenize(tokenized_text)
        for sentence in sentences:
            i = i+1
            print(str(i) + ".cümle: " + sentence)
            res = sum([i.strip(string.punctuation).isalpha() for i in sentence.split()])
            print("Cümledeki Kelime Sayısı: " + str(res))
            kelimesay += res
            print()

            csv_print.writerow([article_name.url, str(i), sentence, str(res)])

        news=[]








