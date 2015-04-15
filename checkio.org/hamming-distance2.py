def checkio(n, m):
    m = map(int, bin(m)[2:])
    n = map(int, bin(n)[2:])
    m.reverse()
    m.reverse()
    if len(n) > len(m):
        m[:0] = [0 for _ in range(len(n) - len(m))]
    elif len(m) > len(n):
        n[:0] = [0 for _ in range(len(m) - len(n))]
    couples = filter(lambda couple: couple[0] ^ couple[1], zip(m, n))
    return len(couples)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
