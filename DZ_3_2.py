# 2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную
# работу с числительными, начинающимися с заглавной буквы. Например:
#
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

number_names = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять",
    "eleven": "одинадцать",
    "twelwe": "двенадцать",
    "thirteen": "тринадцать",
    "fourteen": "четырнадцать",
    "fifteen": "пятнадцать",
    "sixteen": "шестнадцать",
    "seventeen": "семнадцать",
    "eighteen": "восемнадцать",
    "nineteen": "девятнадцать",
    "twenty": "двадцать"
}


def num_translate_adv(num):  # создаем функцию
    if (num[0].isupper()):
        num = num.lower()
        return number_names.get(num).capitalize()
    else:
       return number_names.get(num)





print(num_translate_adv('one'))
print(num_translate_adv('Two'))
print(num_translate_adv('fifteen'))
print(num_translate_adv('rerere'))

