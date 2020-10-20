from collections import Counter
from generator import make_randlist 
 

def test_mr_num():
    a = make_randlist()
    assert len(a) == 100


def test_mr_len_bin():
    a = make_randlist()
    flag = True
    for line in a:
        if len(line) != 10:
            flag = False

    assert flag


def test_mr_items():
    a = make_randlist()
    flag = True
    for i in range(100):
        for j in range(10):
            if a[i][j] != 0 and a[i][j] != 1: 
                flag = False

    assert flag


def test_mr_match():
    a = make_randlist()
    b = make_randlist()
    assert a != b


def test_mr_prob(prob=80):
    a = make_randlist()
    b = [0 for _ in range(10)]
    for i in range(100):
        for j in range(10):
            b[j] += a[i][j]

    flag = True 
    for j in range(10):
        if b[j] < 100 - prob or b[j] > prob:
            flag =False

    assert flag 
    

def test_mr_duplic(duplic=5):
    a = make_randlist()
    c = Counter([int("".join(map(str, a[i])), 2) for i in range(100)])
    assert c.most_common()[0][1] < duplic


def test_mr_variat(variat=85):
    a = make_randlist()
    c = Counter([int("".join(map(str, a[i])), 2) for i in range(100)])
    assert len(c) >= variat

