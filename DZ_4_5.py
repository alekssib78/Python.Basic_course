# 5. *(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.
# Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05

import DZ_4_4_1
def currency_rates_arg(argv):
    name_script, currency_rates_arg = argv


if __name__ == '__main__':
    from sys import argv
    module_name, currency_rates_arg = argv
    DZ_4_4_1.currency_rates(currency_rates_arg)