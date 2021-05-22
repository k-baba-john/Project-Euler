#Largest Prime Factor (#3)
#Question: What is the largest prime factor of the number 600851475143 ?
a = 5 #asal
k = 600851475143 #kontrol 
while True:
    b = 1 #a nın asal olup olmadığını test etmek için kullanılan sayı
    for i in range(a):
        b += 1
        if a == b and 600851475143 % a == 0:
            print(a)
            while k % a == 0:
                k = k / a
                print(k)
        elif a % b == 0:
            break
    a += 2
    if k == 1:
        break

 
print("bitti")
print("Sonuç:", a - 2)