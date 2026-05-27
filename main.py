# 1
# n = int(input())
# a = []
# i = 0
# while i < n:
#     a.append(int(input(f"введи количество циклов{i}")))
#     i += 1
#
# babuska = False
# i = 0
# while i < n- 1 :
#     if a[i] == a[i+1]:
#         babuska = True
#         break
#     i += 1
#
# if babuska:
#     print("YES, YES, YES, YES")
# else:
#     print("NO!")

# 2

# a = []
# b = int(input("введи Свое"))
# c = int(input("введи идеал"))
#
# while b != 0:
#     if b > 0:
#         a.append(b)
#     b = int(input())
# print(max(a))

#3

# a = 0
# b = 0
#
# n = int(input())
#
# while n != 0:
#     if n > 0:
#         a += n
#         b += 1
#     n = int(input())
#
# print(a)
# print(b)

# 4

# n = int(input("введи n  "))
# a = []
# i = 0
#
# while i < n:
#     a.append(int(input(f"aada {i}")))
#     i += 1
#
# su = 0
# vs = 0
# i = 0
# while i < n:
#     if a[i] > 0:
#         su += a[i]
#     elif a[i] < 0:
#         vs += a[i]
#     i += 1
#
# print(su)
# print(vs)

# 5

# n = int(input("введи n  "))
# a = []
# i = 0
# while i < n:
#     a.append(int(input(f" {i}")))
#     i += 1
#
# s = 0
# i = 0
# while i < n - 1:
#     if a[i] * a[i + 1] < 0:
#         s += 1
#     i += 1
#
# print(s)

# 6

# k = int(input("масивы да"))
# n = int(input("элементы на"))
# c = 0
# if n>= 2:
#     for i in range(k):
#         t = []
#         for j in range(n):
#             h= int(input())
#             t.append(h)
#         e = True
#         for j in range(n - 1):
#             if t[j] > t[j + 1]:
#                 e = False
#         if e == True:
#             c += 1
#             print("ок")
#         else:
#             print("не оке")
# print(c)
