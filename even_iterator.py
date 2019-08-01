#!/usr/bin/python3

class Even:
    """Iterator for looping over even or uneven positions"""
    def __init__(self, data, even=True):
        self.data = iter(data)
        self.even = even

    def __iter__(self):
        return self

    def __next__(self):
        if self.even:
            val = next(self.data)
            try:
                next(self.data)
            except StopIteration:
                pass
            return val
        else:
            next(self.data)
            return next(self.data)

