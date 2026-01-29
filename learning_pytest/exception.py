def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class SkipIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lst):
            raise StopIteration

        value = self.lst[self.index]
        self.index += 2
        return value


def skip_iterator(lst):
    return SkipIterator(lst)

it = skip_iterator([1, 2, 3, 4, 5, 6])

for item in it:
    print(item)

