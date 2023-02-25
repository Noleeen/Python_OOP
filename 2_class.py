class Selector:
    def __init__(self):
        self.odd = []
        self.even = []
        self.values = [int(input('input values: ')) for _ in range(int(input('input length of list: ')))]

    def get_odds(self):
        c = self.values
        for i in range(len(c)):
            if c[i] % 2 != 0:
                self.odd.append(c[i])
        return self.odd

    def get_evens(self):
        d = self.values
        for i in range(len(d)):
            if d[i] % 2 == 0:
                self.even.append(d[i])
        return self.even


a = Selector()


print(a.values)
print(a.get_odds())
print(a.get_evens())
