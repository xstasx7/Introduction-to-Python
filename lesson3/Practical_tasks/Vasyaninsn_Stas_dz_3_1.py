# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

# number_list = [2, 3, 5, 9, 3]
# num_index = []
# for index in range(len(number_list)):
#   if index % 2 == True:
#     num_index.append(number_list[index])
# print(sum(num_index))

def numbers(lists):
    num_lists = []
    for index in range(len(lists)):
        if index % 2 == True:
            num_lists.append(lists[index])
    print(sum(num_lists))


numbers([2, 3, 5, 9, 3, 1])
