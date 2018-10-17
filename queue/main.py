from Q import myQueue

x = myQueue()

x.enqueue(6)
print("first item", x.checkFirstItem())
x.enqueue(7)
print("first item", x.checkFirstItem())
print("last", x.checkLastItem())
x.enqueue(8)
print("first item", x.checkFirstItem())
print("last", x.checkLastItem())

x.enqueue("bogdan")
print("first item", x.checkFirstItem())
print("last", x.checkLastItem())
x.iter()
print("size before remove", x.size())
print("removed", x.dequeue())
print("size after remove", x.size())
x.iter()
print("removed", x.dequeue())
x.iter()
print("size after remove", x.size())
