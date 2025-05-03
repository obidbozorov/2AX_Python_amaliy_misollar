class Auto:
    ishlab_chiqarilgan_yili=1950
    rangi='Oq'
    yurgan_masofasi=0
    motor_hajmi=1.5
class Yuk_mashinasi(Auto):
    YukKutarishXajmi=5000
    Kuzov_uzunligi=8
class YengilMashina(Auto):
    tezligi=200
    gildirakbazasi=120
    UrindiqSoni=5
    Kuzov_uzunligi = 4
class Universal_mashina(Yuk_mashinasi,YengilMashina):
    nomi="Universal Machine"
Eshak_Arava=Universal_mashina()
Eshak_Arava.
# QandaydirAuto=Auto()
# QandaydirAuto.rangi="OQ"
# QandaydirAuto.motor_hajmi=5
# print(QandaydirAuto.motor_hajmi, "   ",
#       QandaydirAuto.yurgan_masofasi, QandaydirAuto.YukKutarishXajmi)
Isuzi80=Yuk_mashinasi()
Isuzi80.Kuzov_uzunligi=12
Isuzi80.yurgan_masofasi=5000
print(Isuzi80.rangi)
print(Isuzi80.)