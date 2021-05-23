print(65 * 33 * 15 * 7 + 45 * 66 + 3 + 5 + 6 + 9 + 4950)

total = 0
bolunen_sayı = int(input("Kaça kadar hesaplasın: "))
for i in range(bolunen_sayı):
  if i % 3 == 0 or i % 5 == 0:
    total += i
print(total)
#Hem daha hızlı hem de input istiyor.
#Önceki senin hızlandırdığın koda bir madde ekledim, yoksa çalışmıyordu.

'''
0. satır → 0  3  5  6  9  10 12
1. satır → 15 18 20 21 24 25 27 = 15 15 15 15 15 15 15 + 0  3  5  6  9  10 12
2. satır → 30 33 35 36 39 40 42 = 30 30 30 30 30 30 30 + 0  3  5  6  9  10 12
.
.
.
65. satır → 975 ...
66. satır → 990 990 990 990 990 ___ ___ + 0  3  5  6  9  __ __

990 = 66 × 15

(1 + 2 + ... + 65) × 15 × 7 + 45 × 66 + 3 + 5 + 6 + 9 + 990 × 5
= 65 * 33 * 15 * 7 + 45 * 66 + 3 + 5 + 6 + 9 + 4950

(ilk_sayı + sonuncu sayı ) /  2 * (en büyük sayı/ en küçük sayı)
'''
