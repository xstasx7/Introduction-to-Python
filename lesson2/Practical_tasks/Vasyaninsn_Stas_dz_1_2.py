#2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num_n = int(input("Введите число N: "))
sum_n = 1
composition = []
for i in range(1, num_n + 1):
    sum_n *= i
    composition.append(sum_n)
# print(composition, end='')
if __name__ == "__main__":
    print(composition)
