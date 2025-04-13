# class Person:
#     Ismi = "Ali"
#     Familiyasi="Valiyev"
#     def display_info(self, tili):
#         if tili=="o'zbek":
#             print("Salom, mening ismim", self.Ismi, self.Familiyasi)
#         else:
#             print("Hello",self.Ismi,self.Familiyasi)
# person1 = Person()
# person1.name="Vali"
# print(person1.display_info('o\'zbek'))
# print(person1.display_info(tili='Ingliz'))
class Talaba:
#Konstruktor
    def __init__(self, name,kursi,universiteti="O'zMU"):
        self.name = name # ismni name
        self.kurs=kursi
        self.univer="O'zMU"
        self.stipendiyasi=800000



    def display_info(self):
       print("Salom, mening ismim", self.name, f"  {self.univer}da {self.kurs}-"
                                               f"kursida o'qiyman va {self.stipendiyasi} so'm stipendiya olaman", )
Diyorbek = Talaba(kursi=2, name="Diyorbek",universiteti="Moliya")
Diyorbek.display_info()
del Diyorbek
print(Diyorbek.name)
