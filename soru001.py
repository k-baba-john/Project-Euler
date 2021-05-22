# Multiples of 3 and 5 (#1)
total=0
a=3 # a'nın özel bir anlamı yok

# t ne a ne? Anlamıyorum. Değişken adları daha açıklayıcı olsun.
# Okunabilir kod yazmak çok önemli. (Bilgisayar olimpiyatları hariç)

while a < 1000:
    total+=a
    a+=3
a=5    
while a < 1000:
    total+=a
    a+=5
a=15
while a < 1000:
    total-=a
    a+=15
print(total)

# Şu şekilde yazsan daha okunaklı olurdu:
total = 0
aday_sayı = 3 # a'nın özel bir anlamı var aslında. Hep vardır.
while aday_sayı < 1000:
  if aday_sayı % 3 == 0 or aday_sayı % 5 == 0:
    total += aday_sayı
  aday_sayı += 1 #programa bunu ekledim    
print(aday_sayı)

# Benim kodum seninkinden daha okunaklı.
# Ama seninki daha hızlı. Neden? Bunu düşün. Cevabı söyle bana.
# Benim okunaklı kodumu hızlandırmanın yolunu düşün.
# Replit'te Shell'e girip şu komutu yazarsan zamanı ölçebilirsin:
# time python soru001.py
# Ne kadar hızlandırabileceği konusunda bir ipucu vereyim: Bilgisayara gerek yok. Hesap makinesiyle bile 5 dakika içinde yapabilirsin.

# Sonra yeni bir program yaz. 1000 sabit olmasın. Kullanıcıdan gelen bir sayı olsun. Yine 3 veya 5'e bölünebilen sayıların toplamını bul. Hem olabildiğince hızlı çalışsın. Hem de okunaklı olsun.
# Bunu soru001_varyant01.py diye kaydet.
# Bunu yapabilirsen, 3 ve 5 de sabit olmasın. Kullanıcıdan gelsin. Yani kullanıcıdan 3 sayı al. Örneğin 4 7 3000. 3000'e kadar 4 veya 7'ye bölünebilen sayıların toplamını yazdır.
# Bunu soru001_varyant02.py diye kaydet.

# İyice coşmak istersen, kullanıcıdan a₁ a₂ a₃ ... ve D sayılarını al. D'den küçük a₁ a₂ a₃ ... ten birine bölünebilen sayıların toplamını bul.
# Bunu soru001_varyant03.py diye kaydet.

# Mümkünse girdileri dosyadan oku.

# Sonra Python'da unit test nasıl yapılıyor ona bakalım.
# https://docs.python.org/3/library/unittest.html

# Ama önce varyant01.
# Bu dosyaları mutlaka bilgisayarına yedekle.