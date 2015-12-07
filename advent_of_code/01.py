from sys import argv


def count_final_floor(braces_mix):
    assert isinstance(braces_mix, str)
    return braces_mix.count('(') - braces_mix.count(')')


if __name__ == '__main__':
    print(count_final_floor(argv[1] if len(argv) > 1 else '((()))'))