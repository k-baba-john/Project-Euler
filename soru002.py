# Stilin hep aynı olmalı.
# Yukarıda a <1000 yazmışsın.
# Aşağıda c < 4000000 yazmışsın.
# < operatörünün etrafında boşluk bırakıp bırakmayacağına karar ver.

# Stilin hep aynı olmalı demiştik.
# Bunun için auto-format kullanmanı tavsiye ederim.
# Metin editörüne sağ tıklayıp "format document"e bas, ya da Ctrl+Shift+I kısayolunu kullan. Dene gör nasıl oluyor.

#        ↓ FIBONACCI olacaktı
#Even Fibanocci Number (#2)
a=1
b=1
c=a+b
t=0
while c < 4000000:
    if c%2 == 0:
        t+=c
        print(c)
    a=b
    b=c
    c=a+b
    
print(t)

# Bu soru üzerinden sana iki kavram tanıtmak istiyorum.
# 1- Recursion (özyineleme)
# 2- Memoization: https://en.wikipedia.org/wiki/Memoization
# Bunları oku. Fibonacci programını özyineleme ve memoization ile yazmaya çalış. Python'un kendi memoization araçlarını kullanma. Başaramayacağını düşünüyorum ama yine de yapmanı istiyorum; çünkü seninle beraber başına oturup bakmadan önce senin problemi anlamış olman gerekiyor. Bunun yolu da deneyip başaramamaktan geçiyor. Başarabilirsen zaten bakmamıza gerek yok.
# Burada cevap var bu arada: https://www.python-course.eu/python3_memoization.php
# Ama kopya çekmeden önce mutlaka kendin dene.


# Bu arada dictionary nedir bilmiyorsan buna bak, lazım olacak:
my_dict = {
  (1,2): 'bir ve iki',
  (1,1): 'bir ve bir',
  (5,3): 'beş ve üç',
}
print(my_dict[(1,2)])
print(my_dict[(1,1)])
print(my_dict[(5,3)])
print(my_dict.keys())
print((1,1) in my_dict.keys())
print((10,10) in my_dict.keys())
if (1,1) in my_dict.keys():
  print('(1,1) varmış.')