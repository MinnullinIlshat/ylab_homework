import functools

def memo_decorator(func):
    @functools.wraps(func)
    def wrapper(arg):
        if arg not in wrapper.dict:
            wrapper.dict[arg] = func(arg)
        return wrapper.dict[arg]
    wrapper.dict = {}
    return wrapper

@memo_decorator
def multiplier(number: int):
    return number * 2

