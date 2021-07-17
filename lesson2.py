print('\n1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.')
my_list = ['один', 10, 2.25, [5, 15], (1,2), 'пять', False, None]
for el in my_list:
    print(type(el))

print('\n2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами \n0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте.\n Для заполнения списка элементов нужно использовать функцию input().')

my_list = input('Enter number with space: ')
my_list_1 = my_list.split(' ')

for i in range(1, len(my_list_1), 2):
    my_list_1[i - 1], my_list_1[i] = my_list_1[i], my_list_1[i-1]
print(my_list_1)


print('\n3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.')

month = int(input('Enter number between 0-12: '))
while 0 >= month > 12:
    month = int(input('Error. Enter number between 0-12: '))
else:
    if 0 < month <= 12:
        if 3 <= month < 6:
            print('It is spring')
        elif 6 <= month < 9:
            print('It is summer')
        elif 9 <= month < 12:
            print('It is autumn')
        else:
            print('It is winter')
    else:
        print('error')


mounths = ['winter', 'spring', 'summer', 'autumn']

if 0 < month <= 12:
    if 3 <= month < 6:
        print(f'It is {mounths[1]}')
    elif 6 <= month < 9:
        print(f'It is {mounths[2]}')
    elif 9 <= month < 12:
        print(f'It is {mounths[3]}')
    else:
        print(f'It is {mounths[0]}')
else:
    print('error')

print('\n4.Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.')

name = input('Введитe строку из нескольких слов: ')

n = name.split(' ')

new_list = []
for el in n:
    new_list.append(el[:10])

for el in enumerate(new_list):
    print(el)

print('\n5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо\n запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же\n значением должен разместиться после них.')
"""Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]."""


my_list = [7, 5, 3, 3, 2]
print(my_list)
n = 0
try:
    while n != 'q':
        n = int(input(" Enter number: "))
        i = 0
        for el in my_list:
            if el >= n:
                i += 1
        my_list.insert((i), n)
        print(my_list)
except ValueError:
    print('Это не число. Выходим.')

print('\n6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.')

"""Пример готовой структуры:
[

(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})

]"""

print('\nНеобходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.')

"""Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}
"""

products = []
analytics_name = []
analytics_price = []
analytics_count = []
analytics_unit = []

while input("Нажмите 'Q' для выхода из программы: ").upper() != "Q":
    name = input('Enter new product name: ')
    price = input('Enter new product price: ')
    count = input('Enter new product count: ')
    unit = input('Enter new product unit: ')
    products.append({"название": name, "цена": price, "количество": count, "eд": unit})
    for i in enumerate(products, 1):
        print(f'product structure: {i}')

    analytics_name.append(name)
    analytics_price.append(price)
    analytics_count.append(count)
    analytics_unit.append(unit)

    analytics = dict({'название': analytics_name,
                      'цена': analytics_price,
                      'количество': analytics_count,
                      'ед': analytics_unit})

    print(f'product analytics: {analytics}')
