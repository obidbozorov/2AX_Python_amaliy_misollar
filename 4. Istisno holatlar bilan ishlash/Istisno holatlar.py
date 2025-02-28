# str = "hello"
# number = int(str)
# print(number)
# str = input("Satr kiriting:")
# number = int(str)
# # print(number)
# try:
#     son = int(input("Sonni kiriting: "))
#     print("Kiritilgan son:", son)
# except:
#     print("O`girish noto`g`ri amalga oshirildi.")
# print("Dastur tugadi.")
# try:
#     son = int(input("Sonni kiriting: "))
#     son2=5/son
#     print("Kiritilgan son:", son2)
#
# except ValueError:
#     print("O`girish noto`g`ri amalga oshirildi.")
# except:
#     print("Boshqa turdagi xatolik")
#
# # print("Dastur tugadi.")
# try:
#     son1 = int(input("Birinchi sonni kiriting: "))
#     son2 = int(input("Ikkinchi sonni kiriting: "))
#     print("Bo`lish natijasi:", son1/son2)
# except ValueError:
#     print("O`girish muaffaqiyatsiz amalga oshirildi.")
# except ZeroDivisionError:
#     print("Nolga bo`lish yuzaga keldi.")
# except Exception:
#     print("Umumiy istisno holati.")
# print("Dastur tugadi.")
# try:
#     son1 = int(input("Birinchi sonni kiriting: "))
#     son2 = int(input("Ikkinchi sonni kiriting: "))
#     print("Bo`lish natijasi:", son1/son2)
# except Exception as xatolik:
#     print("Quyidagi xatolik yuz berdi:", xatolik)
# print("Dastur tugadi.")
try:
    insonyoshi=int(input("Yoshni kiriting: "))
    if insonyoshi>=0 and insonyoshi<150:
        print("Insonning yoshi: ", insonyoshi)
    else:
        raise Exception("Inson yoshi manfiy qiymat yoki 150 dan yuqori bo'lishi mumkin emas!")
except ValueError:
    print("Yosh maydoniga raqam kiriting.")
except Exception as Xatolik:
    print(Xatolik)


