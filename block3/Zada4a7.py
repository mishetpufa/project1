import math
import random

class Calculator:
    def calculate_operation(self):
        operation = input("Введите символ операции (+, -, /, *, **, mod, rand, fact, arccos): ")

        if operation == '+':
            return self.perform_addition()
        elif operation == '-':
            return self.perform_subtraction()
        elif operation == '/':
            return self.perform_division()
        elif operation == '*':
            return self.perform_multiplication()
        elif operation == '**':
            return self.perform_exponentiation()
        elif operation == 'mod':
            return self.perform_modulo()
        elif operation == 'rand':
            return self.generate_random_number()
        elif operation == 'fact':
            return self.calculate_factorial()
        elif operation == 'arccos':
            return self.calculate_arccos()
        else:
            print("Неподдерживаемая операция")
            return None

    def perform_addition(self):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        return num1 + num2

    def perform_subtraction(self):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        return num1 - num2

    def perform_division(self):
        num1 = float(input("Введите делимое число: "))
        num2 = float(input("Введите делитель: "))
        return num1 / num2

    def perform_multiplication(self):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        return num1 * num2

    def perform_exponentiation(self):
        num = float(input("Введите число: "))
        power = float(input("Введите степень: "))
        return num ** power

    def perform_modulo(self):
        num1 = float(input("Введите число: "))
        num2 = float(input("Введите модуль: "))
        return num1 % num2

    def generate_random_number(self):
        return random.random()

    def calculate_factorial(self):
        num = int(input("Введите число: "))
        return math.factorial(num)

    def calculate_arccos(self):
        num = float(input("Введите число: "))
        return math.acos(num)


calculator = Calculator()
result = calculator.calculate_operation()

if result is not None:
    print("Результат:", result)