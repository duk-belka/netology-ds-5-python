"""
Простые задания

1. Даны 2 строки long_phrase и short_phrase. Напишите код,
который проверяет действительно ли длинная фраза long_phrase длиннее короткой short_phrase.
И выводит True или False в зависимости от результата сравнения.

long_phrase = 'Насколько проще было бы писать программы, если бы не заказчики'
short_phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

2. Дана строка text. Определите какая из двух букв встречается в нем чаще - 'а' или 'и'.
text = 'Если программист в 9-00 утра на работе, значит, он там и ночевал'

P. S. Вам может помочь метод replace.

3. Дано значение объема файла в байтах. Напишите перевод этого значения в мегабайты в формате:
'Объем файла равен 213.68Mb'

4. Выведите на экран значение синуса 30 градусов с помощью метода math.sin.

5. В прошлом задании у вас скорее всего не получилось точного значения 0.5 из-за конечной точности вычисления синуса.
Но почему некоторые простые операции также могут давать неточный результат?
Попробуйте вывести на экран результат операции 0.1 + 0.2


Задания посложнее
В переменных a и b записаны 2 различных числа. Вам необходимо написать код,
который меняет значения a и b местами без использования третьей переменной.

Дано число в двоичной системе счисления: num=10011.
Напишите алгоритм перевода этого числа в привычную нам десятичную систему счисления.
Возможно, вам понадобится цикл прохождения всех целых чисел от 0 до m:
for n in range(m)
"""


# 1
def assert_first_longer(first_phrase, second_phrase):
    return len(first_phrase) > len(second_phrase)


long_phrase = 'Насколько проще было бы писать программы, если бы не заказчики'
short_phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

print('1)', assert_first_longer(long_phrase, short_phrase))


# 2
def count_use_in_string(key_string, data_string):
    return len(data_string) - len(data_string.replace(key_string, ''))


text = 'Если программист в 9-00 утра на работе, значит, он там и ночевал'
fist_variant = 'а'
second_variant = 'и'
if count_use_in_string(fist_variant, text) > count_use_in_string(second_variant, text):
    print('2) Чаще {}'.format(fist_variant))
else:
    print('2) Чаще {}'.format(second_variant))


# 3
def byteToMb(weight):
    return weight / (1024 * 1024)


print('3) Объем файла равен {}Mb'.format(byteToMb(1048576)))

# 4
import math

print('4)', math.sin(30 * math.pi / 180))  # 0.49999999999999994

# 5
print('5)', 0.1 + 0.2)  # 0.30000000000000004
print('  ', (1 + 2) / 10)  # 0.3

# 6
a = 3
b = 8
print('6)', a, b)
a = a + b
b = a - b
a = a - b
print('  ', a, b)


# 7
def from2to10(num):
    num = str(num)[::-1]
    length = len(num)
    result = 0
    i = 0
    for i in range(length):
        result += int(num[i]) * (2 ** i)

        i += 1
    return result


num_in_2 = 10011
print('7)', from2to10(num_in_2))
