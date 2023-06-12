string = input("Введите произвольную строку: ")

# Проход по всем символам строки
for index, char in enumerate(string):
    if index == 2:
        continue  # Пропускаем 3-й символ
    if char == 'с':
        print("В строке есть символ 'с'")

length = len(string)  # Получаем длину строки
if length > 0:
    print("Длина строки:", length)

if length > 1:
    print("Строка без последнего символа:", string[:-1])