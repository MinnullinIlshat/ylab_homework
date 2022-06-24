from math import factorial

def zeros(n):
    """сравниваем длину строки с нулями в конце, и без них"""
    s = str(factorial(n))
    return len(s) - len(s.strip('0'))

if __name__ == '__main__':
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7

