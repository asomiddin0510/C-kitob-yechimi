# 1-masala.
# a = int(input('a = '))
# if a > 0 :
#     print(a + 1)
# else:
#     print(a)
from signal import pthread_sigmask

from wheel.metadata import yield_lines

# 2-masala.
# a = int(input('a = '))
# if a > 0 :
#     print(a + 1)
# else:
#     print(a - 2)



# 3-masala.
# a = int(input('a = '))
# if a > 0 :
#     print(a + 1)
# elif a < 0 :
#     print(a - 2)
# else:
#     print(10)



# 4-masala.
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# n = 0
# if a > 0 :
#     n += 1
# if b > 0 :
#     n += 1
# if c > 0 :
#     n += 1
# print(n)



# 5-masala.
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# musbat = 0
# manfiy = 3
# if a > 0 :
#     manfiy -= 1
#     musbat += 1
# if b > 0 :
#     manfiy -= 1
#     musbat += 1
# if c > 0 :
#     manfiy -= 1
#     musbat += 1
#
# print(musbat, 'ta musbat son bor ', manfiy, 'ta manfiy son bor')




# 6-masala.
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b :
#     print('katta son ', a)
# else:
#     print('katta son ', b)




# 7-masala.
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b :
#     print(2)
# else:
#     print(1)




# 8-masala.
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b :
#     print(a, ' >>> ', b)
# else:
#     print(b, ' >>> ', a)



# 9-masala.
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b :
#     a , b = b , a
#     print('a = ', a, 'b = ',  b)
# else:
#     print('a = ', a, 'b = ',  b)



# 10-masala.
# a = int(input('a = '))
# b = int(input('b = '))
# if a != b :
#     a = a + b
#     b = a
#     print(a, b)
# elif a == b :
#     a = 0
#     b = 0
#     print(a , b)



# 12-masalam.
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# if a > b and c > b :
#     print(b)
# elif a > c and b > c :
#     print(c)
# else :
#     print(a)




# 13-masala.
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# if (a < b < c) or (c < b < a) :
#     print(b)
# elif (b < c < a) or (a < c < b) :
#     print(c)
# else:
#     print(a)



# 14-masala.
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# if a > b and a > c :
#     eng_kat = a
# elif c > a and c > b :
#     eng_kat = c
# else:
#     eng_kat = b
#
# if a > c and b > c :
#     eng_kic = c
# elif c > b and a > b :
#     eng_kic = b
# else:
#     eng_kic = a
#
# print(eng_kic, eng_kat)



# 15-masala.
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# rezult = a + b
# if rezult < a + c :
#     rezult =a + c
# if rezult < b + c :
#     rezult = b + c
# print(rezult)




# 16-masala.
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# if a < b < c :
#     print(2*a, 2*b, 2*c)
# else:
#     print(-a, -b, -c)



# 17-masala.
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# if (a < b < c) or (c< b < a) :
#     print(2*a, 2*b, 2*c)
# else:
#     print(-a, -b, -c)



# 18-masala.
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# if a == b :
#     print(c, 'ning tartib raqami 3')
# elif b == c :
#     print(a, 'ning tartib raqami  1')
# else :
#     print(b, 'ning tartib raqami 2')




# 19-masala.
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# d = int(input('d = '))
# if a == b == c :
#     print(4)
# elif a == b == d :
#     print(3)
# elif a == c == d :
#     print(2)
# elif b == c == d :
#     print(1)
# else:
#     print('Xarxil sonlar uchtasi bir xil bo\'lishi kerak')




# 20-masala.
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# if abs(a - b) < abs(a - c) :
#     print(a, 'nuqtaga ', b, 'nuqta yaqin va ular orasidagi masofa ', abs(a - b))
# elif abs(a - b) > abs(a - c) :
#     print(a, 'nuqtaga', c,  'eng yaqin nuqta va ular orasidagi masofa ', abs(a - c))
# else:
#     print('Qayta kiritb urinib ko\'ring')



# 21-masala.
# x = int(input('x = '))
# y = int(input('y = '))
# if x == 0 and y == 0 :
#     print(0)
# elif x == 0 and y != 0 :
#     print(1)
# elif y == 0 and x != 0 :
#     print(2)
# else:
#     print(3)



# 22-masala.
# x = int(input('x = '))
# y = int(input('y = '))
# if x > 0  and y  > 0 :
#     print('1-chorak')
# elif x > 0 and 0 > y :
#     print('4-chorak')
# elif x < 0 and y < 0 :
#     print(3)
# else:
#     print(2)



# 23-masala.
# x1 = int(input('x1 = '))
# y1 = int(input('y1 = '))
# x2 = int(input('x2 = '))
# y2 = int(input('y2 = '))
# x3 = int(input('x3 = '))
# y3 = int(input('y3 = '))
# if x1 == x2 and y1 == y3 :
#     x4 = x3
#     y4 = y2
# elif x1 == x3 and y2 == y3 :
#     x4 = x2
#     y4 = y1
# elif x3 == x2 and y3 == y1 :
#     x4 = x1
#     y4 = y2
# print(x4, y4)




# A
# nuqtasi: (2, 3)
# B
# nuqtasi: (2, 7)
# C
# nuqtasi: (6, 7)
# D
# nuqtasi: (6, 3)



# 24-masala.
# import math
# x = int(input('x = '))
# if x > 0 :
#     print(2 * math.sin(x))
# elif x <= 0 :
#     print(x - 6)




# 25-masala.
# x = int(input('x = '))
# if x < -2 or x > 2 :
#     print(2 * x)
# else:
#     print(-3 * x)



# 26-masala.
# x = int(input('x = '))
# if x <= 0 :
#     print(-x)
# elif 0 < x < 2 :
#     print(x ** 2)
# elif x >= 2 :
#     print(4)




# 27-masala.
# x = int(input('x = '))
# if x < 0 :
#     print(0)
# elif 0<= x < 1 or 2 <= x < 3 :
#     print(1)
# elif 1 <= x < 2 or 3 <= x < 4 :
#     print(-1)



# 28-masala.
# yil = int(input('Yilni kiriting : '))
# if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0) :
#     print(366)
# else:
#     print(365)


# 29-masala.
# son = int(input('Son kiriting : '))
# if son > 0 and son % 2 == 1 :
#     print('musbat toq son')
# elif son > 0 and son % 2 == 0 :
#     print('musbat juft son')
# elif son < 0 and son % 2 == 1 :
#     print('manfiy toq son ')
# elif son < 0 and son % 2 == 0 :
#     print('manfiy juft son')
# else:
#     print('nolga teng')




# 30-masala.
# son = int(input('1 dan 999 gacha son kiriting : '))
# if 1 <= son <= 9 and son % 2 == 0 :
#     print('Bir xonali juft son ')
# elif 10 <= son <= 99 and son % 2 == 0 :
#     print('Ikki xonali juft son ')
# elif 100 <= son <= 999 and son % 2 == 0 :
#     print('Uch xonali juft son')
#
# elif 1 <= son <= 9 and son % 2 == 1 :
#     print('Bir xonali toq son')
# elif 10 <= son <= 99 and son % 2 == 1 :
#     print('Ikki xonali toq son')
# elif 100 <= son <= 999 and son % 2 == 1 :
#     print("Uch xonali toq son")






















































