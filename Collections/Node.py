
class Node:

    def __init__(self, value, prev, next):
        self._value = value
        self._prev = prev
        self._next = next

    def __str__(self):
        return str(self._value)
