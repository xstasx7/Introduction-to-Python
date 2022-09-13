# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# nums = [2, 3, 4, 5, 6]
# result = []
# while len(nums) > 1:
#     result.append(nums[0]*nums[-1])
#     del(nums[0], nums[-1])
# if len(nums):
#     result.append(nums[0]**2)
# print(result)


def nums_sum(nums):
    result = []
    while len(nums) > 1:
        result.append(nums[0] * nums[-1])
        del (nums[0], nums[-1])
    if len(nums) == True:
        result.append(nums[0] ** 2)
    print(result)


numbers = [2, 3, 4, 5, 6, 10, 2]
nums_sum(numbers)
