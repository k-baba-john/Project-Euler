def kabul(sayi):
  return sayi % 3 == 0 or sayi % 5 == 0
print(sum(filter(kabul, range(1000))))