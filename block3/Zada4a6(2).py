def create_word_set(words_list):
    words = words_list.split(",")
    return set(words)

def get_word_lengths(word_set):
    word_lengths = []
    for word in word_set:
        word_length = len(word.strip())
        word_lengths.append(word_length)
    return word_lengths

def create_dictionary(word_set, word_lengths):
    return dict(zip(word_set, word_lengths))

def main():
    words_list = input("Введите список слов через запятую: ")
    word_set = create_word_set(words_list)
    print("Количество слов в списке: ", len(word_set))

    word_lengths = get_word_lengths(word_set)
    dictionary = create_dictionary(word_set, word_lengths)
    print("Словарь: ", dictionary)

main()