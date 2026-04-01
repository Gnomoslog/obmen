# задание 1
# a = int(input("число a"))
# b = int(input("число т"))   

# print(a ** b)

# задание 2

a = int(input("число a"))
b = int(input("число т"))   

def bab(a, b):
    if a == 0:
        return b
    else:
        return bab(a - 1, b + 1)
print(bab(a, b))