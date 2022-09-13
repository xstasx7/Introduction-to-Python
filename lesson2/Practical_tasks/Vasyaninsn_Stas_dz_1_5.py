# 5. Реализуйте алгоритм перемешивания списка.

spisok = input("Введите список через запятую: ")
list_name = spisok.split(',')
list_set = set(list_name)
list_random = list(list_set)

if __name__ == "__main__":
    print(list_random)
