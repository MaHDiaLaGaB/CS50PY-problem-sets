import emoji
import time

class Jar:
    def __init__(self, capacity: int=12):
        if capacity < 0:
            raise ValueError("wrong")
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return f"{emoji.emojize(':cookie:') * self.size}"


    def deposit(self, n):
        if self.size + n > self.capacity or n > self.capacity:
            raise ValueError("exceeds capacity")
        self._size = self._size + n



    def withdraw(self, n):
        if self.size < 0 or n > self.size:
            raise ValueError("too many")
        self._size = self._size - n


    @property
    def capacity(self):
        return self._capacity

    # @capacity.setter
    # def capacity(self, capacity):
    #     if capacity > 12:
    #         raise ValueError("too mauch")
    #     self._capacity = capacity

    @property
    def size(self):
        return self._size
