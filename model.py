import bs4 as bs
import re
import gensim
import nltk
nltk.download('stopwords')

scrapped_data = open("C:/Users/asus/PycharmProjects/webScraping/veriler/data.csv", "r", encoding="utf8")
article = scrapped_data .read()

parsed_article = bs.BeautifulSoup(article,'lxml')

processed_article = article.lower()
processed_article = re.sub('[^a-zA-Z]', ' ', processed_article )
processed_article = re.sub(r'\s+', ' ', processed_article)

# Preparing the dataset
all_sentences = nltk.sent_tokenize(processed_article)

all_words = [nltk.word_tokenize(sent) for sent in all_sentences]

# Removing Stop Words
from nltk.corpus import stopwords
for i in range(len(all_words)):
    all_words[i] = [w for w in all_words[i] if w not in stopwords.words('turkish')]

from gensim.models import Word2Vec

word2vec = Word2Vec(all_words, min_count=2)

vocabulary = word2vec.wv.vocab
#print(vocabulary)
#print(word2vec)
#darp, yaralama, korona, kovid, bekliyor
model1 = gensim.models.Word2Vec([vocabulary], min_count=1,
                                size=100, window=5)
print(" 'darp' ve 'yaralama' kelimelerinin arasındaki benzerlik(CBOW): " , model1.wv.similarity('darp', 'yaralama'))
print(" 'korona' ve 'kovid' kelimelerinin arasındaki benzerlik(CBOW): " , model1.wv.similarity('korona', 'kovid'))
print(" 'bekliyor' ve 'korona' kelimelerinin arasındaki benzerlik(CBOW): " , model1.wv.similarity('bekliyor', 'korona'))
print(" 'kovid' ve 'yaralama' kelimelerinin arasındaki benzerlik(CBOW): " , model1.wv.similarity('kovid', 'yaralama'))
print(" 'darp' ve 'kovid' kelimelerinin arasındaki benzerlik(CBOW): " , model1.wv.similarity('darp', 'kovid'))