from random import choice, randint

MIN_LEN = 4
MAX_LEN = 7
VOWELS = 'aeiou'
CONSONANT = 'ABCDEFGHIKLMNOPQRSTVXYZ'.lower()
# rus_alpha = {chr(i) for i in range(ord('а'), ord('я') + 1)}
# VOWELS = ''.join({'а', 'у', 'е', 'ё', 'о', 'э', 'я', 'и', 'ю'})
# CONSONANT = ''.join(rus_alpha.difference(VOWELS))


def random_name(min_len=MIN_LEN, max_len=MAX_LEN):
    name = ''
    for position in range(randint(min_len, max_len)):
        if position % 2:
            name += choice(VOWELS)
        else:
            name += choice(CONSONANT)
    return name.capitalize()

