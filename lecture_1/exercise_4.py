


def bananas(s, banana='banana') -> set:
    result = list()

    if len(s) < len(banana) or (len(s) == len(banana) and s != banana):
        return set()
    string = ['-'] * len(s)
    i = 0
    for j in range(len(banana)):
        for c in range(i, len(s)):
            if banana[j] == s[c]:
                string[c] = banana[j]
                current = ''.join(string)
                if current.replace('-', '') == banana:
                    result.append(current)
                    while banana[-1] in s[c+1:]:
                        string[c] = '-'
                        for q in range(c+1, len(s)):
                            if s[q] == banana[-1]:
                                string[q] = banana[-1]
                                current = ''.join(string)
                                if current.replace('-', '') == banana:
                                    result.append(current)
                                    c = q
                i = c + 1
                break
    return result

def get_first_after(string, symbol):
    """возвращает первую букву и её индекс
    после минимум 1 буквы и 1 символа"""
    l = list(string)
    print(l)
    index = len(string)
    x, y = 0, 0  
    while True:
        index -= 1
        c = l.pop()
        if c.isalpha(): x = 1
        if c == symbol: y = 1
        if c.isalpha() and all((x, y)):
            return c, index


def b_a_n_a_n_a(s, last_obj):
    l_obj = list(last_obj)
    letter, index = get_first_after(last_obj, '-')



print(bananas('bbananana'))
print(get_first_after('b---anana', '-'))