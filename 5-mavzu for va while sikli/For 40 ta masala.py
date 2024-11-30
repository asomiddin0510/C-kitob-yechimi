# 1-masala.
# k = int(input("Biror son kiriting : "))
# n = int(input("Yuqoridagi sonni nechamarta chiqarishni istaysiz : "))
#
# for i in range(n) :
#     print(k)



# 2-masala.
# a = int(input("a = "))
# b = int(input("b = "))
#
# n = 0
# if b > a :
#     for i in range(a , b + 1) :
#         n += 1
#         print(i)
#     print(n, 'ta son chiqqarildi')
#
# else:
#     print("a soni b sonidan kichik bo'lishi kerak")



# 3-masala.
# a = int(input("a = "))
# b = int(input("b = "))
#
# if a < b :
#     n = 0
#     for i in range(a + 1, b ) :
#         n += 1
#         print(i)
#     print(n, 'ta son chiqarildi')
# else:
#     print('b soni a sonidan katta bo\'lishi kerak')



# 4-masala.
# narx = int(input("Bir kilogram konfetning narxni kiriting (ming so'm) : "))
#
# for i in range(1, 11) :
#     rezult = i * narx
#     print(i, 'kg konfetning narxi ', rezult, 'ming bo\'ladi')



# 5-masala.
# narx = int(input("Bir kg konfetning narxni kiriting : "))
# kg_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
#
# for i in kg_list :
#     rezult = i * narx
#     print(i, 'kg konfet narxi : ', rezult)




# 6-masala.
# narx = int(input("Bir kg konfet narxni kiriting : "))
#
# kg_list = [1, 1.2, 1.4, 1.6, 1.8, 2]
# for i in kg_list :
#
#     rezult = narx * i
#     print(i , 'kg konfet narxi : ', rezult)



# 7-masala.

# a = int(input("a = "))
# b = int(input("b = "))
# if a < b :
#     yigindi = 0
#     for i in range(a , b) :
#         yigindi += i
#     print(yigindi)
# else:
#     print("Xato! Siz kiritgan son a soni b sonidan kichik bo'lishi kerak")



# 8-masala.
# a = int(input("a = "))
# b = int(input("b = "))
#
# if a < b :
#     kopaytma = 1
#     for i in range(a, b) :
#         kopaytma *= i
#     print(kopaytma)
# else:
#     print("Xato!")



# 9-masala.
# a = int(input("a = "))
# b = int(input("b = "))
# if a < b :
#     kv_yigindi = 0
#     for i in range(a, b) :
#         kv_yigindi += i ** 2
#     print(kv_yigindi)
# else:
#     print("Xato!")




# 10-masala.
# n = int(input("n = "))
# if n > 0 :
#
#     yigindi = 0
#     for i in range(1, n) :
#
#         yigindi += (1 / i)
#     print(yigindi)
#
# else:
#     print("Xato!")




# 11-masala.
# n = int(input("n = "))
# if n > 0 :
#     yigindi = 0
#     for i in range(0, n + 1) :
#         yigindi += (i + n) ** 2
#     print(yigindi)
# else:
#     print("Xato!")




# 12-masala.
# n = int(input("a = "))
# if n > 0 :
#     kopaytma = 1.0
#     k = 1.0
#     for i in range(1, n + 1) :
#         k += 0.1
#         print(k)
#         kopaytma *= k
#     print("Natija: ", round(kopaytma, 1))
# else:
#     print("Xato!")





# 13-masala.
# n = int(input("n = "))
# if n > 0 :
#     yigindi = 0
#     x =   1.1
#     for i in range(1, n+1) :
#         yigindi += x
#         x = (- 1 ) * (abs(x) + 0.1) * int(x / (abs(x)))
#         x = round(x, 1)
#     print("Natija: ", round(yigindi, 1))
# else:
#     print("Xato!")




# 14-masala.
# n = int(input("n = "))
# if n > 0 :
#     kv = 0
#     for i in range(1, n + 1) :
#         kv += 2 * i -1
#         print(kv)
# else:
#     print("Xato!")




# 15-masala.
# a = float(input("Asos: "))
# n = int(input("Darajasi: "))
#
# kop = 1
# for i in range(1, n + 1) :
#     kop *= a
# print(int(kop))



# 16 - masala.
# a = int(input("Asosni kiriting: "))
# n = int(input("Darajani kiriting: "))
#
# if n > 0 :
#     for i in range(1, n + 1) :
#         print(a**i)
# else:
#     print("Xato!")




# 17-masala.
# a = int(input("Asosni kiriting : "))
# n = int(input("Darajani kiriting : "))
#
# if n > 0 :
#     daraja_yi = 1
#     for i in range(1, n + 1) :
#         x = a ** i
#         print(x)
#         daraja_yi += x
#     print("Natija: ", daraja_yi)
# else:
#     print("Xato!")




# 18-masala.
# a = float(input("Asosni kiriting: "))
# n = int(input("Darajasni kiriting: "))
#
# if n > 0 :
#     daraja_yi = 1
#
#     for i in range(1, n + 1) :
#         k = (-1)**i * a ** i
#
#         daraja_yi += k
#     print("Natija: ",daraja_yi)
#
# else:
#     print("Xato!")




# 19-masala.
# n = int(input("Nechi foktaryalni hisoblamoqchisiz: "))
# if n > 0 :
#     fok_y = 1
#     for i in range(1, n + 1) :
#         fok_y *= i
#     print(fok_y)
# else :
#     print("Xato!")




# 20-masala.# 1 + 2 + 6 + 24 + 120 + 720
# n = int(input("n = "))
# if n > 0 :
#
#     yigindi = 0
#     fok_y = 1
#
#     for i in range(1, n + 1) :
#         fok_y *= i
#
#         yigindi += fok_y
#     print("Natija: ", yigindi)
#
# else:
#     print("Xato!")




# 21-masala.
# n = int(input("n = "))
# if n > 0 :
#     yigindi = 1
#     fok_y = 1
#     for i in range(1, n + 1) :
#         fok_y *= i
#         print(fok_y)
#         yigindi += 1 / int(fok_y)
#     print(yigindi)
# else:
#     print("Xato!")



# 22-masala.
# n = int(input("n = "))
# x = float(input("x = "))
# if x > 0 :
#     yigindi = 1
#     fok_y = 1
#     for i in range(1, n + 1) :
#         fok_y *= i
#
#         yigindi += (x ** i) / int(fok_y)
#
#     print(yigindi)
# else:
#     print("Xato!")



# 23-masala.

n = int(input("n = "))
a = float(input("a = "))

if n > 0 :
    yigindi = 0
    fok_y = 1
    for i in range(1, n + 1) :

        for s in range(1, 2 * i + 2) :
            fok_y *= s
        fok = fok_y
        yigindi += -1*(-1)**i *(a**(2*i+1)) / fok
    print(yigindi)

else:
    print("Xato!")




































































































