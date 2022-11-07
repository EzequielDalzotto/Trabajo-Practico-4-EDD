from typing import Any
from .data_structures import ArrayHeap

class HeapQueue:

    def __init__(self) -> None:
        self._heap = ArrayHeap()
        self._elements = 0

    def first(self) -> Any:
        if self.is_empty():
            raise Exception("La cola esta vacía")

        return self._heap.min()
        

    def enqueue(self,value : Any):
        self._elements+=1
        self._heap.add(self._elements, value)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise Exception("La cola esta vacía")

        retorno = self._heap.min()
        self._heap.remove_min()

        return retorno


    def is_empty(self) -> bool:
        return self._heap.is_empty()

    def __str__(self) -> str:
        return str(self._heap)

    