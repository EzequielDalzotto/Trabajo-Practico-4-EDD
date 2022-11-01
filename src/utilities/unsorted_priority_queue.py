from typing import Any, Tuple
from .unsorted_priority_queue_abstract import UnsortedPriorityQueueAbstract
from .data_structures import PriorityQueueBase

class UnsortedPriorityQueue(UnsortedPriorityQueueAbstract,PriorityQueueBase):
    def __init__(self) -> None:
        self._data = []

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self) == 0

    def add(self, k: Any, v: Any) -> None:
        self._data.append(self._Item(k,v))

    def min(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("La estructura esta vacía")

        min_value = self._data[0]
        for i in self._data:
            if min_value > i: 
                min_value = i
        return (min_value._key, min_value._value)

    def remove_min(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("La estructura esta vacía")

        min_value = self._data[0]
        for i in self._data:
            if min_value > i: 
                min_value = i
                
        self._data.remove(min_value)
        return (min_value._key, min_value._value)