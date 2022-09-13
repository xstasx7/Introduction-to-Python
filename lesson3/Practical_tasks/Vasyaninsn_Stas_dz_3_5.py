# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, -1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# n = int(input("Введите число Фибоначчи: "))
# a = 0
# b = 1
# fib_num = [0]
# for i in range(n):
#     a, b = b, a + b
#     fib_num.append(a)
# c = 0
# d = -1
# for x in range(n):
#     c, d = d, c + d
#     fib_num.insert(0, c)
# print(fib_num)


n = int(input("Введите число: "))
a = 0
b = 1
fib_num = [0]
for i in range(n):
    a, b = b, a + b
    fib_num.append(a)
c = 0
d = -1
fib = []
for x in range(n):
    c, d = d, c + d
    fib_num.insert(0, c)
print(fib_num)
