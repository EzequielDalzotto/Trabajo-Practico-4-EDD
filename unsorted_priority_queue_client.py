from src import UnsortedPriorityQueue

queue = UnsortedPriorityQueue()

queue.add(2,"primero")
queue.add(3,"segundo")
queue.add(4,"tercero")
queue.add(1,"cuarto")
queue.add(3,"quinto")


print("Longitud: ", len(queue))

print("Esta vacia: ", queue.is_empty())

print("Min: ", queue.min())

print("Min removido: ", queue.remove_min())

print("Longitud: ", len(queue))