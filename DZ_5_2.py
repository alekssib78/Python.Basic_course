# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.


def odd_nums(num = int):
    odd_nums_to = [i for i in range(1, num +1 , 2)]  # геннерация списка
    print(odd_nums_to) # выведет весь список сразу
odd_nums(15)

def odd_nums(num=int):
    odd_nums_to = (i for i in range(1, num + 1, 2))
    print(*odd_nums_to)
    print(next(odd_nums_to))
odd_nums(10)