"""
Написать программу, которая:
- Создаёт с помощью генератора списков, список случайных целых чисел от -50 до 50 размером 25 элементов.
- Находит количество положительных, отрицательных и нулевых элементов в списке.
- Выводит значения и их (*положительных, отрицательных и нулевых*) количество вместе с процентом от общего количества.
- Выводит самое большое и самое маленькое значение
"""
import random #Библиотека
list = [random.randint(-50, 50) for i in range(25)]
anable = 0 
negativ = 0
zero = 0
zero_percent = 0
negativ_percent = 0
anable_percent = 0
anable_list = []
negativ_list = []
zero_list = []
min = 0
max = 0
for i in list: #Перебор i в list
    if i < 0: #Условие
        negativ += 1
        negativ_list.append(i) #Добавляем негативный элемент в список негативных 
        if i < min: #Поиск минимального
            min = i
    if i > 0:
        anable += 1
        anable_list.append(i)
        if i > max:
            max = i
    if i == 0:
        zero += 1
        zero_list.append(i)
zero_percent = zero / 25 * 100 #Процент нулей
negativ_percent = negativ / 25 * 100 #Процент  негативных
anable_percent = anable / 25 * 100 #Процент положительных
print(f"Положительные элементы: {anable_list} и их количество:{anable} их процент от общего числа: {anable_percent}")
print(f"Отрицательные элементы: {negativ_list} и их количество:{negativ} их процент от общего числа: {negativ_percent}")
print(f"Нулевые элементы: {zero_list} и их количество:{zero} их процент от общего числа: {zero_percent}")
print(f"Самый минимальный элемент: {min}")
print(f"Самый максимальный элемент: {max}")
