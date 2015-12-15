import hashlib
from sys import argv


def count_final_floor(prefix):
    i = 0
    while i < 10 ** 20:
        if hashlib.md5(''.join((prefix, str(i))).encode()).hexdigest()[:6] == '000000':
            return i
        i += 1


if __name__ == '__main__':
    print(count_final_floor(argv[1] if len(argv) > 1 else 'bgvyzdsv'))