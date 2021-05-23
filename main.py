''' 
Amaç: Replit'te tepedeki "Run ▶" tuşuna bastığında son değiştirdiğin dosyanın çalıştırılması.

Böylece shell'e bir şey yazmayacaksın.

Ayrıca programın çalışma süresini de görüntülüyor.
'''

# *.py diyerek Python dosyalarını listeleyebilmek için:  
import glob

# os, yani operating system.
# İşletim sisteminden dosya özelliklerini alabilmek için.
# Biz değiştirme zamanını alacağız.
import os

# Python dosyalarının listesini al.
python_dosyaları = glob.glob('*.py')

# Değiştirilme zamanına göre sırala (erkenden geçe).
# lambda kullandım. Fonksiyonel paradigma. Bunlara geleceğiz.
python_dosyaları.sort(key=lambda x: os.stat(x).st_mtime)

# Listedeki sonuncu eleman son değiştirilen dosyadır.
son_değiştirilen_dosya = python_dosyaları[-1]

# Son değiştirilen dosya bu dosyaysa sondan ikinci dosyayı seç.
# Çünkü böyle yapmazsan bu dosya sonsuza kadar kendini çağırır.
if son_değiştirilen_dosya == 'main.py':
  son_değiştirilen_dosya = python_dosyaları[-2]

# İstersen bu satırı etkinleştirerek manual override yapabilirsin:
# (İngilizce hazırlıksın, "manual override" ifadesini öğren.)
# son_değiştirilen_dosya = 'soru001_fonksiyonel_paradigma.py'

# time.time ile sistem saatini 2 defa okuyacağım.
# Biri programı çalıştırmadan önce, diğeri sonra.
# İkisinin farkı programının çalışma süresini verir.
# timeit modülü bu iş için daha gelişmiş bir yöntem.
# Ama biz şimdilik böyle yapalım.
import time
print('ÇALIŞTIRIYORUM: ' + son_değiştirilen_dosya)
with open(son_değiştirilen_dosya, 'r') as f:
  içerik = f.read()
  baş = time.time()
  exec(içerik)
  son = time.time()
print('BİTTİ')
# Virgülden sonra 3 haneye yuvarla. Sonrası zaten hiç hassas değil.
print('%.3f saniye sürdü.' % (son - baş))

"""
#---------------------------------------------------------#


#Largest Palindrome Product (#4)
#Find the largest palindrome made from the product of two 3-digit numbers.
car1 = 999 #carpan1
car2 = 999 #carpan2
palist = [] #palindrome number list
while True:
    ori = car1 * car2 #original
    rev = 0 #reverse
    for i in range(len(str(ori))):
        a = ori % 10
        rev = rev * 10 + a
        ori = ori // 10
    ori = car1 * car2    
    if rev == ori:
        palist.append(ori)
        
    if car1 != 100:
        car1 -= 1
    else:
        car1 = 999
        car2 -= 1

    if car2 == 500:
        break

palist.sort(reverse = True)
print("Sonuç:", palist[0])

# 1- Kodun okunurluğu kötü değil. Ama daha iyi olabilirdi.
# Döngünün başındaki kısım `def isPalindrome(number)` diye bir fonksiyon olsa daha okunur olurdu.
# 2- Liste tutmana gerek yok? Senden sadece en büyük palindromu istiyor. `en_büyük` diye bir değişkenin olsa, buldukça güncellesen yeter.
# 3- Madem liste tuttun, son elemanı almak için ters çevirmene gerek yok?
# palist[-1] ile de son elemana ulaşabilirsin.
# 4- break kullanman ve 999'dan geriye doğru sayman güzel. Fakat...
# 100×999'un 600×998'den küçük olacağı bariz.
# Yani önce 2. çarpanı 999'da sabit tutup 1. çarpanı 100'e kadar taraman yanlış.
# {a×b|a,b∈{100,101,...,999}} kümesini büyükten küçüğe taramak için daha hızlı bir yol bulmaya çalış.
# Zamanını ölçünce daha kısa çıkması gerek.
# Eğer böyle bir yol bulabilirsen, büyükten küçüğe taradığın için listeye de gerek kalmayacak. İlk bulduğun palindrom en büyüktür.
# 5- Yine ameleliği bilgisayara yaptırıyorsun. 
# Geçen sefer gösterdiğim gibi matematiksel analiz yapıp bilgisayarın iş yükünü azaltmaya çalış.
# Örneğin çok basit bir geliştirme önereyim. Çarpanlardan birinin 920 olamayacağı belli. Çünkü çarpımın son hanesi 0 olurdu. Palindromun da ilk hanesi 0 olurdu. Ama 0'la başlayan sayı yok. Demek ki çarpanlar 10'a bölünemez. Çarpımın palindrom olup olmadığını kontrol etmekle boşuna vakit kaybediyorsun.

# Yenisini yazınca bu kodu silme.
# Kalitesiz kodlarını da kaydet ki gelecekte karşılaştırabilesin.
# Ayrıca yenisini çalışma sürelerini de karşılaştırabilmelisin.
# "Bence hızlı çalışıyordur" demek yetmez

# Bu arada yazdığın koda epey kulp taktım ama güzel olmuş.
# İlk başladığımız güne kıyasla bile daha okunaklıydı.
# Mükemmele olabildiğince yaklaşmaya çalışıyorum.

#---------------------------------------------------------#
 

#Smallest multiple (#5)
print("Sonuç:", 16*9*5*7*11*13*17*19)


#---------------------------------------------------------#


#Sum Square Difference (#6)
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
total1 = 0
total2 = 0
for i in range(100):
    total1 += (i + 1) ** 2
    total2 += (i + 1)
print("Sonuç:", total2 ** 2 - total1)


#---------------------------------------------------------#


#10001st Prime (#7)
prilist = [2,3,5,7,9]
a = 10

while len(prilist) != 10002:
    b = 2

    if a % 2 == 0 or  a % 5 == 0:
        b = a   
    while a > b:
        if  a % b == 0 :
            break
        b += 1
        if a == b:
            prilist.append(a)
    print(len(prilist))
    a += 1 
print("Sonuç:", prilist[10001])

"""