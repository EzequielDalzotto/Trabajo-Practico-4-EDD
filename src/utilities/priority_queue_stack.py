from .unsorted_priority_queue import UnsortedPriorityQueue
from typing import Any

class PriorityQueueStack:

    def __init__(self) -> None:
        self._queue = UnsortedPriorityQueue()
        self._cont = 0

    def is_empty(self):
        return self._cont == 0

    def push(self,value : Any) -> None:
        self._cont -= 1
        self._queue.add(self._cont, value)

    def pop(self):
        if self.is_empty():
            raise Exception("La pila esta vacía")

        self._cont += 1
        return self._queue.remove_min()

    def top(self):
        if self.is_empty():
            raise Exception("La pila esta vacía")

        return self._queue.min()

    def __len__(self):
        return len(self._queue)

    def __str__(self) -> str:
        res = ""
        for elem in self._queue._data[::-1]:
            res += str(elem) + ", "
        return "PriorityQueueStack(" + res[:-2] + ")"

    def __repr__(self) -> str:
        return str(self)
        
