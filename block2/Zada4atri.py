import math
import random

operation = input("Введите символ операции (+, -, /, *, **, mod, rand, fact, arccos): ")

if operation == '+':
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 + num2
elif operation == '-':
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 - num2
elif operation == '/':
    num1 = float(input("Введите делимое число: "))
    num2 = float(input("Введите делитель: "))
    result = num1 / num2
elif operation == '*':
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 * num2
elif operation == '**':
    num = float(input("Введите число: "))
    power = float(input("Введите степень: "))
    result = num ** power
elif operation == 'mod':
    num1 = float(input("Введите число: "))
    num2 = float(input("Введите модуль: "))
    result = num1 % num2
elif operation == 'rand':
    result = random.random()
elif operation == 'fact':
    num = int(input("Введите число: "))
    result = math.factorial(num)
elif operation == 'arccos':
    num = float(input("Введите число: "))
    result = math.acos(num)
else:
    print("Неподдерживаемая операция")
    result = None

if result is not None:
    print("Результат:", result)