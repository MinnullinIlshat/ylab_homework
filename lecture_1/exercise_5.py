from itertools import combinations_with_replacement

def get_product(numbers):
    """принимает список чисел, возвращает результат их уможения"""
    result = 1
    for i in numbers:
        result = result * i 
    return result

def is_in_limit(numbers, limit):
    """принимает список чисел, если резултат их умножения меньше
    чем limit возвращает True"""
    return get_product(numbers) <= limit

def numbers_in_comb(numbers, comb):
    for num in numbers:
        if num not in comb:
            return False
    return True

def get_combinations(numbers, limit, length):
    result = []
    for comb in combinations_with_replacement(numbers, length):
        if  numbers_in_comb(numbers, comb) and is_in_limit(comb, limit):
            current = sorted(comb)
            if current not in result:
                result.append(current)
    return result

def get_set_combinations(numbers, limit, max_length):
    result = []
    for i in range(len(numbers), max_length + 1):
        result.extend(get_combinations(numbers, limit, i))
    return result

def count_find_num(primesL, limit):
    if not is_in_limit(primesL, limit):
        return []
    primesL.sort()
    results = [primesL]
    longest = primesL[:]
    longest.append(primesL[0])
    while is_in_limit(longest, limit):
        results.append(longest[:])
        longest.append(primesL[0])
    longest = longest[:-1]
    max_length = len(longest)
    combinations = get_set_combinations(primesL, limit, max_length)
    products = [get_product(i) for i in combinations]
    return [len(products), max(products)]