Bu projede nltk, article, bs4, gensim kütüphanesi kullanılarak ilk aşamada
internetteki haber sitelerinden güncel haberler çekilmiştir. 
Çekilen haberler öncelikle cümlelerine, ardından kelimelerine ayrıştırılmıştır.
dataScraping.py dosyası çalıştırıldığında ekran çıktısı olarak ayrıştırılmış
haber metinlerini, her cümlenin metinde kaçıncı satırda yer aldığını, cümlelerdeki
toplam kelime sayısını ve haber metinlerinin url adresini verir. 
model.py dosyasında ise haber metinlerde geçen kelimeler kullanılarak bir sözlük
oluşturulmuştur. Ve bu kelimelerden birkaçı seçilerek aralarındaki benzerlik
oranları(CBOW) hesaplanmıştır. Kendi seçtiğim kelimeler için benzerlik oranları 
word dosyası şeklinde proje ile birlikte yüklenmiştir.