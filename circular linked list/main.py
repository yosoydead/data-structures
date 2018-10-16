from circularLinkedList import CLL

x = CLL()

x.add(7)
print("head", x.head.data, "tail", x.tail.data)
x.add(5)
print("head", x.head.data, "tail", x.tail.data)
x.add(3)
print("head", x.head.data, "tail", x.tail.data)
x.add(1)
print("head", x.head.data, "tail", x.tail.data)
x.add("bogdan")
print("head", x.head.data, "tail", x.tail.data)
x.add("radu")
print("head", x.head.data, "tail", x.tail.data)
x.iter()