# 1 dan n gacha bo'lgan sonlar yig'indisini toping
# n=int(input("n="))
# a=["Ali","Vali","Gani"]
# for ismlar in a:
#     print(ismlar)
import random

# sum=1
# for i in range(n):
#     sum=sum*i
#     print(i,sum)
# print("sum=",sum)
#Berilgan natural sonlar ketma-ketligida tartib nomeri Fibonachchi sonlari bo'lgan hadlarining yig'indisini hisoblaydigan programma tuzilsin.
n=int(input("n="))
i=1
sum=0
f1=1
f2=2
f3=3
sonn=random.randint(1,20)
sum=sum+sonn
print(i,"=",sonn)
for i in range(2,n+1):
    sonn=random.randint(1,20)
    print(i,"=",sonn)
    if i==f2:
        f3=f1+f2
        f1=f2
        f2=f3
        sum = sum + sonn
        print("Navbatdagi fibonachi soni=",sonn)
print("sum=",sum)


