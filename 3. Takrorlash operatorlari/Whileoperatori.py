# 1 dan n gacha bo'lgan sonlar yig'indisini toping
# n=int(input("n="))
# sum=0
# i=1
# while i<0:
#     sum=sum+i
#     i=i+1
# print("Summ=",sum)

# Berilgan natural n va m uchun hisoblansin: 3-masala .
n=int(input("n="))
m=int(input("m="))
sum=0
p=1
i=1
j=5
while i<=n:
    while j<=m:
        p=p*(i+j)
        j=  j+1
    sum=sum+p
    i=i+1
    p=1
    j=5

print("S=",sum)
