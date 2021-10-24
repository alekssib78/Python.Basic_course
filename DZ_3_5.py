# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов,
# взятых из трёх списков:
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#         Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
#  (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы
# именованными?

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


# def get_jokes(num = int):
#
#     for i in range(num):
#         nouns_ind = random.choice(nouns)
#         adverbs_ind = random.choice(adverbs)
#         adjectives_ind = random.choice(adjectives)
#         print(nouns_ind, adverbs_ind, adjectives_ind)
#
#
# get_jokes(4)

# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
#  (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы
# именованными?


def get_jokes_uniq(rate=int, unique=False): # если нужны уникальные шутки unique=True
    if unique:
        for i in range(rate):
            nouns_ind = random.choice(nouns)
            adverbs_ind = random.choice(adverbs)
            adjectives_ind = random.choice(adjectives)
            print(nouns_ind, adverbs_ind, adjectives_ind)  # после вывода шутки удаляем использованное слово из списков
            nouns.remove(nouns_ind)
            adverbs.remove(adverbs_ind)
            adjectives.remove(adjectives_ind)


    else:
        for i in range(rate):
            nouns_ind = random.choice(nouns)
            adverbs_ind = random.choice(adverbs)
            adjectives_ind = random.choice(adjectives)
            print(nouns_ind, adverbs_ind, adjectives_ind)


get_jokes_uniq(3, True)  # функция ввернет шутки без повторяющихся слов если слова закончатся в списках вернется ошибка
