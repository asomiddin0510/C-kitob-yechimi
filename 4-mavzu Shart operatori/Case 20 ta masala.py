# 1-masala.
# hafta_kunlari = ['Yakshanba','Dushanba', "Seshanba", 'Chorshanba', 'Payshanba', 'Juma', 'Shanba']
# kun = int(input('Raqamni kiriting : '))
# ind = kun % 7
# print("Siz kiritgan raqam ", hafta_kunlari[ind], ' kuniga to\'g\'ri keladi')

# hafta_kunlari = ['Yakshanba','Dushanba', "Seshanba", 'Chorshanba', 'Payshanba', 'Juma', 'Shanba']
# kun = int(input('Son kiriting ; '))
# match kun:
#     case 1 :
#         print("Siz kiritgan raqam Dushanba kuniga to'g'ri keladi ")
#     case 2 :
#         print("Siz kiritgan raqam Seshanba kuniga to'g'ri keladi")
#     case 3 :
#         print("Siz kiritgan raqam Chorshanba kuniga to'g'ri keladi ")
#     case 4 :
#         print("Siz kiritgan raqam Payshanba kuniga to'g'ri keladi")
#     case 5 :
#         print("Siz kiritgan raqam Juma kuniga to'g'ri keladi")
#     case 6 :
#         print("Siz kiritgan raqam Shanba kuniga to'g'ri keladi")
#     case 7 :
#         print("Siz kiritgan raqam Yakshanba kuniga to'g'ri keladi")



# 2-masala.
# baho_n = int(input('Bahoni kiriting (1 dan 5 gacha) : '))
# match baho_n :
#     case 1 :
#         baho_y = "Yomon"
#     case 2 :
#         baho_y = "Qoniqarsiz"
#     case 3 :
#         baho_y = "Qoniqarli"
#     case 4 :
#         baho_y = "Yaxshi"
#     case 5 :
#         baho_y = "Alo"
#     case _ :
#         baho_y = None
#
# if baho_y is not None :
#     print("Siz olgan baho :", baho_y)
# else:
#     print("Siz 1 dan 5 gacha baho kiritishingiz kerak")




# 3-masala.
# oy = int(input('Hozirgi turgan oyingizni kiriting : '))
# match oy :
#     case 1| 2| 3 :
#         print("Siz Qish faslidasiz")
#     case 4| 5| 6 :
#         print("Siz Bahor faslidasiz")
#     case 7| 8| 9 :
#         print("Siz Yoz faslidasiz")
#     case 10| 11| 12 :
#         print("Siz Kuz faslidasiz")




# 4-masala.
# oy_raqam = int(input("Oyning raqamni kiriting (1, 12) : "))
# match oy_raqam :
#     case 3| 4| 9| 11 :
#         kunlar = [30]
#
#     case 1| 5| 7| 8| 10| 12 :
#         kunlar = [31]
#
#     case 2| 6 :
#         kunlar = [29]
#
#     case _ :
#         kunlar = [None]
#
#
# if None not in kunlar :
#     print("Siz kiritgan oyda ", kunlar[0], ' kun bor')
# else:
#     print("Siz kiritgan oy (1, 12) oraliqda bo'lishi kerak! ")




# 5-masala.
# a = int(input('a = '))
# b = int(input('b = '))
# amallar = int(input("1-qo'shish, 2-ayirish, 3-bo'lish, 4-ko'paytrish shu amallardan qaybirini foydalanmoqchisiz : "))
# match amallar :
#     case 1 :
#         rezult = a + b
#     case 2 :
#         rezult = a - b
#     case 3 :
#         if b != 0 :
#             rezult = a / b
#         else:
#             rezult = "Siz b o'zgaruvchisiga 0 bergansiz bu xato !"
#     case 4 :
#         rezult = a * b
#     case _ :
#         rezult = "Siz 1-amaldan 4-amalgacha bajara olasiz"
# print("Natija : ", rezult)




# 6-masala.
# uzunlik = int(input("Uzunlik o'lchovni kiriting : "))
# tan = int(input("1-detsimetr, 2-kilometr, 3-metr, 4-millemetr, 5-santimetr yuqorida kiritgan uzunlik o'lchovni qay brida kiritdingiz tanlang : "))
# match tan :
#     case 1 :
#         rezult = uzunlik / 10
#     case 2 :
#         rezult = uzunlik * 1000
#     case 3 :
#         rezult = uzunlik / 1
#     case 4 :
#         rezult = uzunlik / 1000
#     case 5 :
#         rezult = uzunlik / 100
#     case _ :
#         rezult = [None]
# list = [1, 2, 3, 4, 5]
# if list :
#     print("Siz kiritgan uzunlik o'lchovi metirda : ", rezult, 'teng')
# else:
#     print("Xato kiritdingiz (1 : 5) oraliqda kiriting ")




# 7-masala.
# massa = int(input("Massani kiriting : "))
# tan = int(input("1-kg, 2-mg, 3-g, 4-t, 5-sentner quydagilardan birni tanlang qaysi birini kiritgan bo'lsangiz : "))
# match tan :
#     case 1 :
#         rezult = massa / 1
#     case 2 :
#         rezult = massa * (1/10)**6
#     case 3 :
#         rezult = massa * (1/10)**3
#     case 4 :
#         rezult = massa * 1000
#     case 5 :
#         rezult = massa * 100
#     case _ :
#         rezult = "Xato"
#
# if rezult != "Xato" :
#     print(int(rezult) , "kg ga teng")
# else:
#     print("Xato son kiritdingiz (0, 6) oraliqdan kiriting ")


# 8-masala.
# month = int(input("Oyni raqamni kiriting : "))
# day = int(input("Kunni kiriting : "))
# match month :
#     case 1 :
#         rezult = "Yanvar"
#         rezult1 = 31
#     case 2 :
#         rezult = "Fevrall"
#         rezult1 = 28
#     case 3 :
#         rezult = "Mart"
#         rezult1 = 31
#     case 4 :
#         rezult = "Aprel"
#         rezult1 = 30
#     case 5 :
#         rezult = "May"
#         rezult1 = 31
#     case 6 :
#         rezult = "Iyun"
#         rezult1 = 30
#     case 7 :
#         rezult = "Iyull"
#         rezult1 = 31
#     case 8:
#         rezult = "Avgust"
#         rezult1 = 31
#     case 9 :
#         rezult = "Sentabr"
#         rezult1 = 30
#     case 10 :
#         rezult = "Oktabr"
#         rezult1 = 31
#     case 11 :
#         rezult = "Noyabr"
#         rezult1 = 30
#     case 12 :
#         rezult = "Dekabr"
#         rezult1 = 31
#     case _ :
#         rezult = "Xato"
# if rezult != "Xato" and 1 <= day <= rezult1 :
#     print(day,"-",rezult)
# else:
#     print("Siz xato oy kun raqamni kiritdingiz")





# month = int(input("Oyni raqamni kiriting : "))
# day = int(input("Kunni kiriting : "))
# months = {
#     1: ("Yanvar", 31),
#     2: ("Fevral", 28),
#     3: ("Mart", 31),
#     4: ("Aprel", 30),
#     5: ("May", 31),
#     6: ("Iyun", 30),
#     7: ("Iyul", 31),
#     8: ("Avgust", 31),
#     9: ("Sentabr", 30),
#     10: ("Oktabr", 31),
#     11: ("Noyabr", 30),
#     12: ("Dekabr", 31),
# }
# if 1 <= month <= 12 and 1 <= day <= months[month][1] :
#     print(day, "-", months[month][0])
# else:
#     print("Kun yoki oyning raqami nato'g'ri kiritilgan!")




# # 9-masala.
# month = int(input("Oyni raqamni kiriting : "))
# day = int(input("Kunni kiriting : "))
#
# months = {
#     1 : ("Yanvar", 31),
#     2 : ("Fevral", 28),
#     3 : ("Mart", 31),
#     4 : ("Aprel", 30),
#     5 : ("May", 31),
#     6 : ("Iyun", 30),
#     7 : ("Iyul", 31),
#     8: ("Avgust", 31),
#     9 : ("Sentabr", 30),
#     10 : ("Oktabr", 31),
#     11 : ("Noyabr", 30),
#     12 : ("Dekabr", 31)
# }
#
# if 1 <= month <= 12 and 1 <= day <= months[month][1] :
#     if months[month][1] == day:
#         month += 1
#         day = 1
#     print(day , '-', months[month][0])
# else:
#     print("Xato raqam kiritgansiz!")




# 10-masala.
# yonalish = input("Robot yo'nalishini kiriting (s - shimol, j - janub, q - sharq, g - g'arb) : ").lower()
# kamanda = int(input("Kamandani kiriting (0 - harakat davom, 1 - chapga, 2 - o'nga) : "))
# match yonalish :
#     case "s" :
#         rezult = "Shimol",
#     case "j" :
#         rezult = "Janub",
#     case "q" :
#         rezult = "Sharq",
#     case "g" :
#         rezult = "G'arb",
#     case _ :
#         rezult = None
#
# if rezult is None :
#     print("Nato'g'ri yo'nalish tanladingiz!")
# elif kamanda == 0 :
#     print(rezult[0], "ga bo'lgan yo'lida davom etmoqda")
#
# elif kamanda == 2 :
#     match yonalish :
#         case "s" :
#             new_rezult = "Janub"
#         case "j" :
#             new_rezult = "Sharq"
#         case "q" :
#             new_rezult = "G'arb"
#         case "g" :
#             new_rezult = "Shimol"
#     print(rezult[0], 'dan ', new_rezult, 'ga burildi')
# elif kamanda == 1 :
#     match yonalish :
#         case "s" :
#             new_rezut = "G'arb"
#         case "g" :
#             new_rezult = "Sharq"
#         case "q" :
#             new_rezult = "Janub"
#         case "j" :
#             new_rezult = "Shimol"
#     print(rezult[0], 'dan ', new_rezult, 'ga burildi')




# 11-masala.
# bosh_yonalish = input("Robot yo'nalishini kiriting (s - shimol, j - janub, q - sharq, g - g'arb) : ").lower()
# kamanda = int(input("Kamandani kiriting (0 - o'nga, 1 - chapga, 2 - 180 gradus burlish) : "))
# match bosh_yonalish :
#     case "s" :
#         rezult = "Shimol"
#     case "j" :
#         rezult = "Janub"
#     case "q" :
#         rezult = "Sharq"
#     case "g" :
#         rezult = "G'arb"
#     case _ :
#         rezult = None
#
# if rezult is None :
#     print("Nato'g'ri yo'nalish tanladingiz!")
#
# elif kamanda == 0 :
#     # o'nga burlish kodi
#     match bosh_yonalish :
#         case "s" :
#             new_rezult = "Janub"
#         case "j" :
#             new_rezult = "Sharq"
#         case "q" :
#             new_rezult = "G'arb"
#         case "g" :
#             new_rezult = "Shimol"
#     print(rezult, 'dan ', new_rezult, 'ga burildi')
# elif kamanda == 1 :
#     # Chapga burlish kodi
#     match bosh_yonalish :
#         case "s" :
#             new_rezult = "G'arb"
#         case "g" :
#             new_rezult = "Sharq"
#         case "q" :
#             new_rezult = "Janub"
#         case "j" :
#             new_rezult = "Shimol"
#     print(rezult, 'dan ', new_rezult, 'ga burildi')
# elif kamanda == 2 :
#     match bosh_yonalish :
#         case "s" :
#             new_rezult = "Sharq"
#         case "j" :
#             new_rezult = "G'arb"
#         case "q" :
#             new_rezult = "Shimol"
#         case "g" :
#             new_rezult = "Janub"
#     print(rezult, 'dan', new_rezult, 'ga o\'z yo\'nalishni o\'zgartirdi ')



# 12-masala.
pi = 3.14
# kiritish = float(input("Kiriting : "))
# tur = int(input("Yuqorida kiritgan malumotingiz : "))
# match tur :
#     case 1 :
#         R = kiritish
#     case 2 :
#         R = kiritish / 2
#     case 3 :
#         R = kiritish / (2 * pi)
#     case 4 :
#         R = (kiritish / pi) ** 0.5
#     case _ :
#         R = None
#
# if R is None :
#     print("Xato kiritdingiz ! ")
# else:
#     r = R
#     d = 2 * r
#     l = 2 * pi * r
#     s = pi * r ** 2
#     print(" R = ", r, " D = ", d, " L = ", l, " S = ", s , " teng")




# 13-masala.
# import math
# kirit = float(input("Uchburchakni biror bir elementni kiriting : "))
# tan = int(input("Tanlang qay bir elementni kiritdingiz (1-katet a, 2 gipotenuza, 3-'2-'ga tushirilgan balandlik, 4-yuzasi) : "))
# match tan :
#     case 1 :
#         a = kirit
#     case 2 :
#         a = kirit / (2**0.5)
#     case 3 :
#         a = kirit * (2**0.5)
#     case 4 :
#         a = math.sqrt(2 * kirit)
#     case _ :
#         a = None
#
# if a is None:
#     print("Siz kiritgan raqamda element yo'q!")
# else:
#     a = a    # Katet
#     c = a * (2 ** 0.5)  # Gipotenuza
#     h = c / 2  # Balandlik
#     s = h * c # Yuzasi
#     print('a = ', a, 'c = ', c, 'h = ', h, 's = ', s, ' ga teng ')



# 14-masala.
# import math
# kirit = float(input("Teng tomonli uchburchakning elementni kiriting : "))
# tan = int(input("1-tomoni a, 2-ichki chizilgan aylana radiusi r1, 3-t chizlgan aylana radiusi r2, 4-yuzasi s tanlang : "))
# match tan :
#     case 1 :
#         a = kirit
#     case 2 :
#         a = kirit * 6 / math.sqrt(3)
#     case 3 :
#         a = 12 * kirit / math.sqrt(3)
#     case 4 :
#         a = math.sqrt(kirit/(4/math.sqrt(3)))
#     case _ :
#         a = None
# if a is None :
#     print("Xato! Kiritgan raqamingizni tekshrib qayta kiriting (0 : 5) oraliqda bo'lishi kerak.")
# else:
#     a = a
#     r1 = a * math.sqrt(3) / 6
#     r2 = 2 * r1
#     s = pow(a, 2) * (math.sqrt(3)/4)
#     print('a = ', a, 'r1 = ', r1, 'r2 = ', r2, 's = ', s, 'ga teng')




# 15-masala.
# karta = int(input("Karta qiymatni kiriting : "))
# karta_turi = int(input("Quyda karta turlari va raqamlari berilgan \n(1-g'isht, 2-olma, 3-chillik, 4-qarg'a)\n(11-valet, 12-dama, 13-qirol, 14-tuz) \nqaybrini qiymatni kiritgan bo'lsangiz tanlang : "))
#
# rezult = None
# if karta < 5 :
#     match karta_turi:
#         case 1:
#             rezult = 'g\'isht'
#         case 2:
#             rezult = 'olma'
#         case 3:
#             rezult = 'chillik'
#         case 4:
#             rezult = 'qarg\''
# elif 10 < karta <= 14 :
#     match karta_turi :
#         case 11 :
#             rezult = 'valet'
#         case 12 :
#             rezult = 'dama'
#         case 13 :
#             rezult = 'qirol'
#         case 14 :
#             rezult = 'tuz'
#
#
#
# if rezult is None :
#     print("Xato")
# else:
#     print(karta, rezult)





# 16-masala.
# yosh = int(input("Yoshingizni kiriting: "))
#
# rezult = None
#
# match yosh :
#     case 20 :
#         rezult = "Siz yegirma "
#     case 21 :
#         rezult = "Siz yegirma bir "
#     case 22 :
#         rezult = "Siz yegirma ikki "
#     case 23 :
#         rezult = "Siz yegirma uch "
#     case 24 :
#         rezult = "Siz yegirma to'rt "
#     case 25 :
#         rezult = "Siz yegirma besh "
#     case 26 :
#         rezult = "Siz yegirma olti "
#     case 27 :
#         rezult = "Siz yegirma yetti "
#     case 28 :
#         rezult = "Siz yegirma sakkiz "
#     case 29 :
#         rezult = "Siz yegirma to'qqiz "
#     case 30 :
#         rezult = "Siz o'ttiz "
#     case 31 :
#         rezult = "Siz ottiz bir "
# if rezult is None :
#     print("Xato! ")
# else:
#     print("Tabriklayman", rezult, "yoshdasiz")




#
# yosh = int(input("Yoshingizni butun sonda kiriting : "))
#
#
# birlar = ['bir', 'ikki', 'uch', 'to\'rt', 'besh', 'olti', 'yetti', 'sakkiz', 'to\'qqiz']
# onlar = ["o'n", "yigirma", "o'ttiz", "qirq", "ellik", 'olmish', 'yetmish', 'sakson', "to'qson"]
#
#
# if 1 <= yosh <= 9 :
#     rezult = birlar[yosh-1]
#     print("Tabriklayman siz ", rezult, 'yoshdasiz')
#
# elif 10 <= yosh < 100 :
#     onlar_q = yosh // 10
#     birlar_q = yosh % 10
#
#     if birlar_q == 0 :
#         rezult = onlar[onlar_q - 1]
#         print("Tabriklayman siz ", rezult, 'yoshdasiz')
#
#     else:
#         rezult = onlar[onlar_q - 1] + ' ' + birlar[birlar_q - 1]
#         print("Tabriklayman siz ", rezult, 'yoshdasiz')
#
# elif yosh == 100 :
#     print("Tabriklayman siz ", 100, 'yoshga kiribsiz')
#
# else:
#     print("Xato ! Juda katta yosh (1 ; 100) oraliqda bo'lgan yoshlarga. ")




# 17-masala.
# nomer = int(input("Oxirgi masalaning nomerni kiriting: "))
#
# birlar = ['bir', 'ikki', 'uch', "ro'rt", 'besh', 'olti', 'yetti', 'sakkiz', "to'qqiz"]
# onlar = ["o'n", 'yegirma', "o'ttiz", 'qirq']
#
#
# birlar_q = nomer % 10
# onlar_q = nomer // 10
#
# if birlar_q == 0 and onlar_q in [1, 2, 3, 4] :
#     rezult = onlar[onlar_q - 1]
#     print(rezult, 'ta masala')
#
# elif onlar_q in [1, 2, 3, 4] :
#     rezult = onlar[onlar_q - 1] + ' ' + birlar[birlar_q - 1]
#     print(rezult, 'ta masala')
#
# else:
#     print("Xato! (10 : 40) oralig'ida bo'lishi kerak ")





# 18-masala.
#
# son = int(input("100dan 999 gacha bo'lgan sonlardan kiriting : "))
#
# birlar = ['bir', 'ikki', 'uch', "to'rt", 'besh', 'olti', 'yetti', 'sakkiz', 'to\'qqiz']
# onlar = ["o'n", 'yegirma', "o'ttiz", 'qirq', 'ellik', 'oltmish', 'yetmish', 'sakson', "to'qson"]
# yuz = " yuz "
#
#
# if 100 <= son <= 999 :
#     birlar_q = son % 10
#     onlar_q = (son // 10) % 10
#     yuz_q = son // 100
#     print(birlar_q, onlar_q, yuz_q)
#
#     if birlar_q == 0 and onlar_q == 0 :   #400
#         rezult = birlar[yuz_q - 1] + " " + yuz
#         print(rezult)
#
#     elif birlar_q == 0 : # 440
#         rezult = birlar[yuz_q - 1] + yuz + onlar[onlar_q - 1]
#         print(rezult)
#
#     elif onlar_q == 0 :  # 404
#         rezult = birlar[yuz_q - 1] + yuz + birlar[birlar_q - 1]
#         print(rezult)
#
#     else :  # 489
#         rezult = birlar[yuz_q - 1] + yuz + onlar[onlar_q - 1] + ' ' +  birlar[birlar_q - 1]
#         print(rezult)
#
# else:
#     print("Xato! (100 : 999) oraliqdagi sonlarni kiriting : ")


# 19- masala.

rang = ['yashil', 'qizil', 'sariq', 'oq', 'qora']
hayvonlar = ['schqon', 'sigir', "yo'lbars", 'quyon', 'ajdar', 'ilon', 'ot', "qo'y", 'maymun', "tovuq", 'it', "to'ng'iz"]

yil = int(input("Yilni kiriting : "))
kerak_yil = (yil - 1984) % 60

rang_q = kerak_yil // 12
hayvonlar_q = kerak_yil % 12   # 0, 12, 24, 36, 48, 60


if kerak_yil == 0 :
    rezult = rang[0] + ' ' + hayvonlar[0]

if rang_q == 0 :
    rezult = rang[rang_q] + ' ' + hayvonlar[hayvonlar_q - 1]

elif rang_q == 1 :
    rezult = rang[rang_q] + ' ' + hayvonlar[hayvonlar_q - 1]

elif rang_q == 2 :
    rezult = rang[rang_q] + ' ' + hayvonlar[hayvonlar_q - 1]

elif rang_q == 3 :
    rezult = rang[rang_q] + ' ' + hayvonlar[hayvonlar_q - 1]

elif rang_q == 4 :
    rezult = rang[rang_q] + ' ' + hayvonlar[hayvonlar_q - 1]

elif rang_q == 5 :
    rezult = rang[rang_q] + ' ' + hayvonlar[hayvonlar_q - 1]

print("Siz kiritgan yil ",rezult, "yiliga teng")


















































