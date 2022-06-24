


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
    b_a_n_a_n_a(s, result[-1])
    return result

def b_a_n_a_n_a(s, last_obj):
    result = list()
    print(s)
    print(last_obj)

print(bananas('bbananana'))

