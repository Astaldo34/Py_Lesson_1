dict_numbers = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(user_number):
    return dict_numbers.get(user_number)


user_num = input("Введите прописью число от 1 до 10 по английски: ")
print(num_translate(user_num))
