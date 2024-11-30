from sys import int_info

# 1-masala.
# l = int(input('l = '))
# metr = l/100
# print(l, 'sm', metr, 'm bo\'ladi')


# 2-masala.
# massa = int(input('massani kg da kiriting : '))
# tonna = massa/1000
# print(massa, 'kg', tonna, 't bo\'ladi ')



# 3-masala.
# bayt = int(input("Baytlarda faylni hajmni kiriting : "))
# kbayt = bayt//1024
# print('Siz bergan fayl hajmi kilobaytlarda : ', kbayt)



# 4-masala.
# a = int(input("Sizdagi uzun kesmani kiriting : "))
# b = int(input("Nechi uzunlikda qilib kesib chiqmoqchisiz : "))
# rezult = a // b
# print('Siz a kesmaning ichiga b kesmani ', rezult, 'marta joylay olasiz')



# 5-masala.
# a = int(input("Sizdagi uzun kesmani kiriting: "))
# b = int(input("Nechi uzunlikdan qilib kesmoqchisiz shuni kiriting : "))
# rezult = a // b
# siqmagan =b - ( a % b )
# print("b kesma a kesmada ", rezult, 'marta joylashdi b dan ', siqmagan, 'qolib ketti')




# 6-masala.
# son = int(input("Ikki xonlai son kiriting: "))
# on = son // 10
# bir = son % 10
# print('O\'nliklar xonasidagi son : ', on, ' birliklar xonasidagi son : ', bir)



# 7-masala.
# son = int(input("Ikki xonali son kiriting : "))
# rezult = son//10 + son%10
# print(rezult)



# 8-masala.
# son = int(input("Ikki xonali son kiriting : "))
# son = (son%10)*10 + son//10
# print(son)



# 9-masala.
# son = int(input("Uch xonali son kiriting : "))
# yuzlar_xonasi = son // 100
# print("yuzlarxonasi : ", yuzlar_xonasi)



# 10-masala.
# son = int(input("Uchxonali son kiriting : "))
# bir = son % 10
# on = (son//10) % 10
# print(bir, on)




# 11-masala.
# son = int(input("Uchxonali son kiriting : "))
# rezult = son // 100 + son % 10 + (son//10)%10
# print(rezult)



# 12-msala.
# son = int(input("Uchxonali son kiriting : "))
# rezult = son//100 + ((son//10)% 10)*10 + (son%10)*100
# print(rezult)



# 13-masala.
# son = int(input("Uchxonali son kiriting : "))
# yuz = son//100
# rezult = (son%100)*10 + yuz
# print(rezult)




# 14 - masala.385  538
# son = int(input("Uchxonali son kiriting : "))
# rezult = ( son % 10 )*100 + son//10
# print(rezult)



# 15-masala. 347   437
# son = int(input("Uch xonali son kiriting : "))
# yuz = son // 100
# on = (son // 10) % 10
# bir = son % 10
# rezult = on * 100 + yuz * 10 + bir
# print(rezult)



# 16-masala.  467    476
# son = int(input("Uchxonali son kiriting : "))
# yuz = son // 100
# on = (son // 10)% 10
# bir = son % 10
# rezult = yuz * 100 + bir * 10 + on
# print(rezult)



# 17-masala.     2846
# son = int(input("999 dan katta son kiriting : " ))
# yuz = (son // 100) % 10
# print(yuz)



# 18-masala.   35678
# son = int(input("999 dan katta son berilgan : "))
# ming = (son // 1000) % 10
# print(ming)



# 19-masala.
# n = int(input("N sekundni kiriting : "))
# min = n // 60
# print('kun boshidan beri ', min, 'daqiqa o\'tdi')



# 20-masala.
# sekun = int(input("Kun boshidan beri o'tgan sekundlarni kiriting : "))
# soat = min // 3600
# print('Kun boshidan beri', soat, ' soat o\'tdi')



# 21-masala.
# sekun = int(input("Kun boshidan beri o'tgan sekundlarni kiriting : "))
# min = sekun // 60
# sekun_q = sekun - min * 60
# print("Kun boshidan beri o'tgan daqiqa va sekundlar", min, ' minud', sekun_q, ' sekund')




# 22-masala.
# n = int(input("Kun boshidan beri qancha sekund o'tdi "))
# soat = n // 3600
# q_daqiqa = n // 60 - soat * 60
# print(soat, ' soat', q_daqiqa, ' daqiqa')



# 23-masala.
# n = int(input("Kun boshidan boshlab n sekund o'tdi shu sekundni kiriting : "))
# soat = n // 3600
# q_daqiqa = n // 60 - soat * 60
# q_sekund = n - (n // 60) * 60
# print(soat, ' soat', q_daqiqa, ' daqiqa', q_sekund, ' sekund')



# 24-masala.
# hafta_kunlar = ['yakshanba', 'dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma', 'shanba']
# k = int(input("1-yanvardan beri necha kun o'tganini kiriting: "))
# ind = (k-1) % 7
# print(hafta_kunlar[ind])



# 25-masala.
# k = int(input("1 - Yanvardan boshlab qancha kun o'tgan bo'lsa shuni kiriting : "))
# hafta_kunlari = ['yakshanba', 'dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma', 'shanba']
# ind = (k % 7 + 4) % 7
# print(hafta_kunlari[ind])



# 26-masala.
# hafta_kunlar = ['dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma', 'shanba', 'yakshanba']
# k = int(input("1-yanvardan necha kun o'tgandan keyingi hafta kunini bilmoqchi bo'lsangiz kiriting : "))
# ind = (k + 1) % 7
# print(hafta_kunlar[ind])



# 27-masala.
# hafta_kunlar = ['dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma', 'shanba', 'yakshanba']
# k = int(input("1-yanvardan necha kun o'tgandan keyingi hafta kunini bilmoqchi bo'lsangiz kiriting (1-yanvar yakshanba) : "))
# ind = (k + 6) % 7
# print(hafta_kunlar[ind])


# 28-masala.
# hafta_kunlar = ['dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma', 'shanba', 'yakshanba']
# kun = int(input('1-yanvar qaysi kunga to\'g\'ri keladi (1, 7) : '))
#
# print('1-yanvar ', hafta_kunlar[kun-1], 'kuniga to\'g\'ri keladi', end = ' ')
# hafta_kun = int(input("1 - 365 oralig'idagi kunni kiriting : "))
#
# ind = (kun + hafta_kun-1) % 7
# print(hafta_kunlar[ind])



# 29-masala.
a = int(input("a = "))
b = int(input('b = '))
c = int(input('c = '))
n = (a*b)//c




















