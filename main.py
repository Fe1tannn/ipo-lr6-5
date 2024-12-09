import random 
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
for i in list:
    if i < 0:
        negativ += 1
        negativ_list.append(i)
        if i < min:
            min = i
    if i > 0:
        anable += 1
        anable_list.append(i)
        if i > max:
            max = i
    if i == 0:
        zero += 1
        zero_list.append(i)
zero_percent = zero / 25 * 100
negativ_percent = negativ / 25 * 100
anable_percent = anable / 25 * 100
print(f"Положительные элементы: {anable_list} и их количество:{anable} их процент от общего числа: {anable_percent}")
print(f"Отрицательные элементы: {negativ_list} и их количество:{negativ} их процент от общего числа: {negativ_percent}")
print(f"Нулевые элементы: {zero_list} и их количество:{zero} их процент от общего числа: {zero_percent}")
print(f"Самый минимальный элемент: {min}")
print(f"Самый максимальный элемент: {max}")