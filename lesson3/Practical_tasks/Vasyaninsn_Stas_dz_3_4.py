# Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# num = int(input("Введите число: "))
# bin_num = ''
# while num > 0:
#     bin_num = str(num % 2) + bin_num
#     num = num // 2
# print(f"В двоичной системе исчесления будет: {bin_num}")

def num_bin(num):
    bin_num = ''
    while num > 0:
        bin_num = str(num % 2) + bin_num
        num = num // 2
    print(f"В двоичной системе исчесления будет: {bin_num}")


num_bin(45)
