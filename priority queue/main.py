from priorityQueue import PriorityQueue

ER = PriorityQueue()

ER.enqueue("common cold", 5)
ER.enqueue("gunshot wound", 1)
ER.enqueue("high fever", 4)
ER.enqueue("broken arm", 2)
ER.enqueue("flu", 3)

print(ER.dequeue())
print(ER.dequeue())
print(ER.dequeue())
print(ER.dequeue())
print(ER.dequeue())

