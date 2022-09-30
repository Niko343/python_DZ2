# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# 6782,0 -> 23
# 0,56 -> 11

n = float(input('Введите число: '))
str_n = str(n)
str_n = str_n.replace('.', '')
list_str = list(str_n)
list_b = map(int, list_str)
s = sum(list_b)
print(s)