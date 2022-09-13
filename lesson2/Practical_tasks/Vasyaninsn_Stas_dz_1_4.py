# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

num_len = int(input('Введите длину списка: '))
num_prod = 1
nums = []
for i in range(num_len):
    num = int(input('Введите элементы списка: '))
    nums.append(num)

for i in nums:
    num_prod *= i

if __name__ == "__main__":
    print(f'Cписок из: {num_len}')
    print(f'Сумма элементов списка равна: {sum(nums)}')
    print(f'Произведение элементов списка равно: {num_prod}')
