number = float(input("Введите произвольное число: "))
boundary = float(input("Введите пограничное число: "))

if number < boundary:
    print("Первое число меньше пограничного")
elif number > boundary:
    print("Первое число больше пограничного")
    if number > boundary * 3:
        print("Первое число больше пограничного более, чем в 3 раза")