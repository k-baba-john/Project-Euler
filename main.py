
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
