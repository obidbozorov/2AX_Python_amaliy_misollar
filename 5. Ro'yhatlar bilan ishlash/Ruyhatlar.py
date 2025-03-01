# k=99
# sonlar1 = [1, "Salom", 3, k,True, [5,5,6,5,6,5,6,6,"SALOM DUNYO!"], 6, 7, 8]
# sonlar2 = list(sonlar1)
# print(sonlar1[4])
#print(sonlar1[-3])
# print(sonlar1[1][1])
# print(sonlar1[3])
# qiriqilgan_ruyhat=sonlar1[1:4]
# qiriqilgan_ruyhat=sonlar1[-4:-1]
# qiriqilgan_ruyhat=sonlar1[:4]
# qiriqilgan_ruyhat=sonlar1[3:]
# yangi_ruyhat=sonlar2*3
# print(yangi_ruyhat)
# n=int(input("n="))
# sonlar_ruyhati=list(range(3,n+1,3))
# print(sonlar_ruyhati)
# poytaxtlar = ['London', 'Parij',['Sidney','Kanberra'],'Moskva', 'Tashkent']
# for poytaxt in poytaxtlar:
#     print(poytaxt)
# poytaxtlar = ['London', 'Parij', 'Moskva', 'Tashkent']
# i = 0
# elementsoni=len(poytaxtlar)
# print("Ro'yhatdagi poytaxtlar soni:",elementsoni)
# while i < len(poytaxtlar):
#     print(poytaxtlar[i])
#     i += 1
# sonlar1 = [1, "Salom", 3, 4, True, [9, 10, 11,12, "SALOM DUNYO!"], 6, 7, 8]
# for son in sonlar1:
#     if type(son)==list:
#         for sonichki in son:
#             print(sonichki)
#     else:
#         print(son)

# nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# nums2 = list(range(10))
# nums3=[9,8,7,6,5,4,3,2,1,0]
# if nums1 == nums3:
#     print("Bu ro`yxatlar aynan teng.")
# else:
#     print("Bu ro`yxatlar teng emas.")
poytaxtlar = ['London', 'Parij','Moskva','Parij', 'Tashkent']
# for poytaxt in poytaxtlar:
#     print(poytaxt)
# poytaxtlar[3]=['Moskva','Sankt-Peterburg']
poytaxtlar.append("Dushanbe")
poytaxtlar.append("Ashgabad")
# print(poytaxtlar)
# poytaxtlar.insert(2,'Rim')
# print(poytaxtlar)
# poytaxtlar.remove("Parij")
# uchirilgan_poytaxt=poytaxtlar.pop(40)
# print("Siz quyidagi poytaxtni o'chirdingiz: ",uchirilgan_poytaxt)
# print(poytaxtlar)
# ashgabad_urni=poytaxtlar.index('Berlin')
# print(ashgabad_urni)
# elementsoni=poytaxtlar.count("Parij")
# print(elementsoni)
# son=[1,2,3,4,5,6,-6,8,9,2,0]
# tartiblangan_ruyhat=list()
# print(tartiblangan_ruyhat)
# son = [1, 2, 3, 4, 5, 6, -6, 8, 9, 2, 0]
# print(min(son))
# # sonteskari=son.reverse()
# print(sonteskari)
# if 'Ashgabad' in poytaxtlar:
#     print("Bor")
# else:
#     print("Yo'q")
# poytaxtlar.sort()
poytaxtlar.sort()
poytaxtlar.reverse()
print(poytaxtlar)