# 2.
# 1.Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
cube_list_of_odd = []

for i in range(1, 1000, 2):
    cube_list_of_odd.append(i ** 3)
print(cube_list_of_odd)

# 2.Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делитсянацело на 7.
# Внимание: использовать только арифметические операции!
sum_appropriate_number = 0
sum_appropriate_number17 = 0

for i in cube_list_of_odd:
    sum_number = 0
    for j in str(i):
        j_run = int(j) % 10
        sum_number += j_run
        j = int(j) // 10
    if sum_number % 7 == 0:
        sum_appropriate_number += int(i)
print(sum_appropriate_number)


# 3.К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых
#     делится нацело на 7. Внимание: новый список не создавать!!!
sum_appropriate_number = 0

for i in cube_list_of_odd:
    i += 17
    sum_number = 0
    for j in str(i):
        j_run = int(j) % 10
        sum_number += j_run
        j = int(j) // 10
    if sum_number % 7 == 0:
        sum_appropriate_number17 += int(i)
print(sum_appropriate_number17)