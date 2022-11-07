from src.utilities.heap_queue import HeapQueue


hp = HeapQueue()

#Test de excepcion
# hp.dequeue()
# hp.first()

print(hp.is_empty())

hp.enqueue("Perro")
hp.enqueue("gato")
hp.enqueue("loro")
hp.enqueue("raton")

print(hp)

print(hp.first())

print(hp.dequeue())

print(hp.first())

print(hp.is_empty())
