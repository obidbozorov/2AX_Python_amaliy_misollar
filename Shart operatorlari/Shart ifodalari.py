# a=7
# b=not (6!=a)
# print(b)
# Masala: 2-kurs talabalarining a'lo baholarda o'quvchilarini ajratib olish
# natija=kurs==2 and min(baholari)==5
# print(natija)
# yoshi = 21
# vazni = 72
# t = True
# natija = yoshi > 17 and vazni > 56 and t
# print(natija)
# yoshi = 22
# xolati = False
# vazni = 58
# natija = vazni == 58 or xolati and not yoshi > 21 # True
# print(natija)

# yoshi = 51
# if yoshi >18:
#     print("Kirishga ruxsat beriladi")
# else:
#     print("Iltimos, ",(18-yoshi), " yil sabr qiling.")
# print("Tamom")
# a= int(input("a="))
# b= int(input("ikkinchi koefisentni kiriting b="))
# c= int(input("c="))
# d = b**2 - 4*a*c
# if d >0:
#     print("Tenglama 2 ta haqiqiy echimga ega")
# elif d == 0:
#     print("Tenglama 1 ta haqiqiy echimga ega")
# else:
#     print("Tenglama haqiqiy echimga ega emas")
protsent = int(input("Protsentni kiriting: "))
if protsent > 10:
    print("10% dan katta")
    if protsent > 20:
        print("20% dan katta")