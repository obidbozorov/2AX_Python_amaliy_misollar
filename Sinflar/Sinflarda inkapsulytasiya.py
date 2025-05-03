class Person:
    def __init__(self, name):
        self.__name = name # ismini o'rnatish
        self.__age = 1  # yoshni o'rnatish

    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Mumkin bo'lmagan yosh")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def display_info(self):
        print("Ism:", self.__name, "\tYosh:", self.__age)
    def set_Tekshirilgan_kursi(self,kursi):
        if kursi>4 or kursi<1:
            print("Mumkin bo'lmagan kurs. Talabaning kursi [1;4] "
                  "oraliqda bo'ladi. Iltimos, tekshirib qaytadan kiriting.")
        else:
            self.__Tekshirilgan_kursi=kursi
    def get_Tekshirilgan_kursi(self):
        return self.__Tekshirilgan_kursi
Nosir=Person("Nosirjon Ruzmetov")
print(Nosir.get_name())

Nosir.set_age(19)
Nosir.set_Tekshirilgan_kursi(2)
print(Nosir.get_Tekshirilgan_kursi())
Nosir.set_Tekshirilgan_kursi(3)
print(Nosir.get_Tekshirilgan_kursi())

