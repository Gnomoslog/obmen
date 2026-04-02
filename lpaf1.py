# задание 1
# a = input("Введите числа через пробел: ")
# b = input("Введите числа через пробел: ")
# arr = list(map(int, a.split()))
# arr = list(map(int, b.split()))
# a_1 = set(a) - set(b)
# a_2 = set(b) - set(a)

# print(a_1)
# print(a_2)


# задание 2

# n = int(input("Введите кол-во элементов списка: "))
# first_list = [int(i) for i in input("Введите значения списка: ").split()[:n]]

# print(sum([first_list[i - 1] < first_list[i] > first_list[i + 1]
#            for i in range(1, n - 1)]))


# задание 3

# numbers = [int(i) for i in input("Введите числа: ").split()]
# count_numbers = {}
# for i in numbers:
#     if i not in count_numbers:
#         count_numbers[i] = 1    
#     else:
#         count_numbers[i] += 1
# print(sum([i // 2 for i in count_numbers.values()]))


# PDF ЗАДАНИЕ 4

# a = int(input("ведите"))
# data = {}
# for i in range(2, a + 1):
#     s = 1
#     for g in range(2, i // 2 + 1):
#         if i % g == 0:
#             s += g
#     data[i] = s
# print(data)