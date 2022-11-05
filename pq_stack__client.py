from src.utilities.priority_queue_stack import PriorityQueueStack

pqs = PriorityQueueStack()

#Prueba de excepcion
# pqs.pop()
# pqs.top()

pqs.push("jorge")
pqs.push("pedro")
pqs.push("nico")

print(pqs)

print(pqs.pop())

print(pqs)

print(pqs.top())
print(pqs)