import functools
import time 

def expo_timer(func_=None, *, call_count=5, start_sleep_time=1, 
            factor=2, border_sleep_time=30):
    def wrapper(func):
        @functools.wraps(func)
        def wrapper_second(*args, **kwargs):
            t = start_sleep_time
            for i in range(1, call_count+1):
                time.sleep(t)
                result = func(*args, **kwargs)
                print(f'Запуск номер {i}. Ожидание: {t} секунд. '
                f'Результат декорируемой функции = {result}.')
                if t >= border_sleep_time: t = border_sleep_time
                else: t *= factor
        return wrapper_second 
    if func_ is None:
        return wrapper
    return wrapper(func_)