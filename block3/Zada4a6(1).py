import math
import random

def calculate_operation():
    operation = input("Введите символ операции (+, -, /, *, **, mod, rand, fact, arccos): ")

    if operation == '+':
        return perform_addition()
    elif operation == '-':
        return perform_subtraction()
    elif operation == '/':
        return perform_division()
    elif operation == '*':
        return perform_multiplication()
    elif operation == '**':
        return perform_exponentiation()
    elif operation == 'mod':
        return perform_modulo()
    elif operation == 'rand':
        return generate_random_number()
    elif operation == 'fact':
        return calculate_factorial()
    elif operation == 'arccos':
        return calculate_arccos()
    else:
        print("Неподдерживаемая операция")
        return None

def perform_addition():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    return num1 + num2

def perform_subtraction():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    return num1 - num2

def perform_division():
    num1 = float(input("Введите делимое число: "))
    num2 = float(input("Введите делитель: "))
    return num1 / num2

def perform_multiplication():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    return num1 * num2

def perform_exponentiation():
    num = float(input("Введите число: "))
    power = float(input("Введите степень: "))
    return num ** power

def perform_modulo():
    num1 = float(input("Введите число: "))
    num2 = float(input("Введите модуль: "))
    return num1 % num2

def generate_random_number():
    return random.random()

def calculate_factorial():
    num = int(input("Введите число: "))
    return math.factorial(num)

def calculate_arccos():
    num = float(input("Введите число: "))
    return math.acos(num)

result = calculate_operation()

if result is not None:
    print("Результат:", result)