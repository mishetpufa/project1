words_list = input("Введите список слов через запятую: ")
words = words_list.split(",")

words_set = set(words)
print("Количество слов в списке: ", len(words_set))

second_list = []
for word in words_set:
    word_length = len(word.strip())
    second_list.append(word_length)

dictionary = dict(zip(words_set, second_list))
print("Словарь: ", dictionary)