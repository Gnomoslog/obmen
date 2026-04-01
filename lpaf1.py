# задание1 
# n = int(input("Ведение знач"))
# a0, a1, = 0, 1
# for i in range(n):
#     a_ne = a0 + a1
#     a0 = a1
#     a1 = a_ne
# print(a_ne)
# задание 2
# n = int(input("Ведение знач"))
# m = [int(i) for i in input("Input m").split()[:n]]
# print([min(m) if i == max(m) else i for i in m])


# задание 3

# def mam_b(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return (n != 1) * True


# print("Yes" if mam_b(int(input("faffsa"))) else "no")


# задание 4 

# def re(n):
#     if n == 0:
#         return ""
#     x = int(input("faffsa"))
#     return re(n - 1) + f" {x}"

# n = int(input("faffsa"))
# print(re(n))
