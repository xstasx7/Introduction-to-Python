# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 0,56 -> 11

number_str = input("Введите число вещественное число: ")
number_lst = []
for i in number_str:
    if i.isdigit():
        number_lst.append(i)
    else:
        continue
count = 0
sum_number = 0
list_length = len(number_lst)
while count < list_length:
    sum_number = sum_number + int(number_lst[count])
    count = count + 1

if __name__ == "__main__":
    print(sum_number)
