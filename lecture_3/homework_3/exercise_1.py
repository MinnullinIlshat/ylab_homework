import functools

def memo_decorator(func):
    @functools.wraps(func)
    def wrapper(arg):
        return wrapper.dict.setdefault(arg, func(arg))
    wrapper.dict = {}
    return wrapper

@memo_decorator
def multiplier(number: int):
    return number * 2

