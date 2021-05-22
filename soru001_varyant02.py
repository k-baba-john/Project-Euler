total = 0
bolunen_sayı = int(input("Kaça kadar hesaplasın: "))
sayi1 = int(input("Katı bulunucak ilk sayı:"))
sayi2 = int(input("Katı bulunucak ikinci sayı:"))
for i in range(bolunen_sayı):
  if i % sayi1 == 0 or i % sayi2 == 0:
    total += i
print(total)