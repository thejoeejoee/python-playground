VOWELS = "AEIOUY"  # True
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"  # False
from re import split, match, I, M, S, X


def checkio(text):
    assert isinstance(text, (str, unicode))
    count = 0
    for word in split(r'\.|\?|,| ', text):
        if not word:
            continue
        if is_word_ok(word):
            count += 1
    return count


def is_word_ok(word):
    pattern = r"""
    ^(([BCDFGHJKLMNPQRSTVWXZ]{1})([AEIOUY]{1}))*([BCDFGHJKLMNPQRSTVWXZ]?)$
    |
    ^(([AEIOUY]{1})([BCDFGHJKLMNPQRSTVWXZ]{1}))*([AEIOUY]?)$
    """
    if len(word) > 1 and match(pattern, word, I + M + S + X):
        return True
    return False


if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert checkio(
        u"To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?") == 8, 'muhaha'