
class CyclicIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)

    def __iter__(self):
        return self 

    def __next__(self):
        try:
            value = next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            value = next(self.iterator)
        return value

if __name__ == '__main__':
    cyclic_iterator = CyclicIterator(range(3))
    for i in cyclic_iterator:
        print(i)
