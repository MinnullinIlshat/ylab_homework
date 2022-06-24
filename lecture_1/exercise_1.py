            
def get_home_url(url):
    """убирает http и/или все что после '/' """
    if url.startswith('http'):
        return url.split('/')[2]
    return url.split('/')[0]

def without_TLD(url):
    """убирает www в начале и домен выского уровня в конце"""
    if url.startswith('www.'):
        url = url.split('.', 1)[1]
    return '.'.join(url.split('.')[:-1])

def get_longest(url):
    """tld практически всегда короче домена, поэтому возвращаем самую длинную строку
    Если нужно сделать точнее можно добавить в список возможные tld и удалить
    их с помощью str.translate() """
    d_list = url.split('.')
    d_list = sorted(d_list, key=len, reverse=True)
    return d_list[0]

def domain_name(url):
    home_url = get_home_url(url)
    result = without_TLD(home_url)
    if '.' not in result:
        return result
    return get_longest(result)

if __name__ == '__main__':
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"

