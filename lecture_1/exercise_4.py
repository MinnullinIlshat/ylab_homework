def is_in(string, letters):
    """проверяет есть ли буквы letters в строке 
    string, расположенные в том же порядке
    (между буквами могут быть другие символы)"""
    letters = list(letters)
    gen = (i for i in string)
    l = letters.pop(0)
    for _ in range(len(string)):
        try: s = next(gen)
        except StopIteration: return False 
        if s == l:
            if not letters:
                return True 
            else:
                l = letters.pop(0)
    return False

class Banana:

    def __init__(self, string='banana'):
        self.string = string 
        self.b_0 = []
        self.a_1 = []
        self.n_2 = []
        self.a_3 = []
        self.n_4 = []
        self.a_5 = []
        self._get_indexes()

    def _get_indexes(self):
        s = self.string
        for i in range(len(self.string)):
            if s[i] == 'b' and is_in(s[i+1:], 'anana'):
                self.b_0.append(i)
            elif s[i] == 'a':
                if 'b' in s[:i] and is_in(s[i+1:], 'nana'):
                    self.a_1.append(i)
                if is_in(s[:i], 'ban') and is_in(s[i+1:], 'na'):
                    self.a_3.append(i)
                if is_in(s[:i], 'banan'):
                    self.a_5.append(i)
            elif s[i] == 'n':
                if is_in(s[:i], 'ba') and is_in(s[i+1:], 'ana'):
                    self.n_2.append(i)
                if is_in(s[:i], 'bana') and is_in(s[i+1:], 'a'):
                    self.n_4.append(i)

    def _get_banan(self, b0, a1, n2, a3, n4, a5):
        dashes = ['-'] * len(self.string)
        dashes[b0] = 'b'
        dashes[a1] = 'a'
        dashes[n2] = 'n'
        dashes[a3] = 'a'
        dashes[n4] = 'n'
        dashes[a5] = 'a' 
        s = ''.join(dashes)
        if s.replace('-', '') == 'banana':
            return s 


    def get_bananas(self):
        bananas = list()
        for b0 in self.b_0: 
            for a1 in self.a_1: 
                for n2 in self.n_2:
                    for a3 in self.a_3:
                        for n4 in self.n_4:
                            for a5 in self.a_5:
                                current = self._get_banan(b0, a1, n2, a3, n4, a5)
                                if current: bananas.append(current)                    
        return set(bananas)

def bananas(s):
    banana = Banana(s)
    return banana.get_bananas()
    
if __name__ == '__main__':
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
