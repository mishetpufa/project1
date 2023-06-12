word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")
word3 = input("Введите третье слово: ")

lowercase_words = [word1.lower(), word2.lower(), word3.lower()]
uppercase_words = [word1.upper(), word2.upper(), word3.upper()]
capitalized_words = [word.capitalize() for word in [word1, word2, word3]]

quantity1 = int(input("Введите количество для {}: ".format(word1)))
quantity2 = int(input("Введите количество для {}: ".format(word2)))
quantity3 = int(input("Введите количество для {}: ".format(word3)))

output = "Данные:\n" \
         "Нижний регистр: {}\n" \
         "Верхний регистр: {}\n" \
         "Первый символ в верхнем регистре: {}\n" \
         "Количество овощей:\n" \
         "{}: {}\n" \
         "{}: {}\n" \
         "{}: {}"

print(output.format(
    ", ".join(lowercase_words),
    ", ".join(uppercase_words),
    ", ".join(capitalized_words),
    word1, quantity1,
    word2, quantity2,
    word3, quantity3
))