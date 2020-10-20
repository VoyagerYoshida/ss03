import random


def make_randlist():
    return [list(map(int, str(bin(random.randrange(2**10))[2:].zfill(10)))) for _ in range(100)]


if __name__ == '__main__':
    l = make_randlist()
    print(*l, sep='\n')

