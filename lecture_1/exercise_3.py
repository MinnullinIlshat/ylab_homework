def zeros(n):
    res = 0
    while n > 0:
        n //= 5
        res += n
    return res
