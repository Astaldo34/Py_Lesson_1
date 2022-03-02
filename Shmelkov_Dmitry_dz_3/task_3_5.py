from random import randrange, choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat='no'):
    """Parses n in cycle that generates a number of jokes, repeat - specifies whether values can be repeated """
    if n > 5 or n < 0:
        return print('Введите значение циклов не менее 1 и не более 5')
    list_joke = []
    for i in range(n):
        if repeat == 'yes':
            list_joke.append(f'{nouns.pop(randrange(len(nouns)))} {adverbs.pop(randrange(len(adverbs)))} '
                             f'{adjectives.pop(randrange(len(adjectives)))}')
        else:
            list_joke.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return print(list_joke)


# print(nouns) check list for changes
get_jokes(3, repeat='yes')
