def kabul(sayi):
  return sayi % 3 == 0 or sayi % 5 == 0
print(filter(kabul, range(2000)))
from time import sleep
sleep(0.33)