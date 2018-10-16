from circularLinkedList import CLL

x = CLL()

x.addToEnd(7)
print("head", x.head.data, "tail", x.tail.data)
x.addToEnd(5)
print("head", x.head.data, "tail", x.tail.data)
x.addToEnd(3)
print("head", x.head.data, "tail", x.tail.data)
x.addToEnd(1)
print("head", x.head.data, "tail", x.tail.data)
x.addToEnd("bogdan")
print("head", x.head.data, "tail", x.tail.data)
x.addToEnd("radu")
print("head", x.head.data, "tail", x.tail.data)
x.addAtTheStartOfTheList("mircea")
print("head", x.head.data, "tail", x.tail.data)
x.addToEnd(54612)
print("head", x.head.data, "tail", x.tail.data)
x.iter()

"""
    head 7 tail 7
    head 7 tail 5
    head 7 tail 3
    head 7 tail 1
    head 7 tail bogdan
    head 7 tail radu
    head mircea tail radu
    head mircea tail 54612
    
    head mircea
    7
    5
    3
    1
    bogdan
    radu
    tail 54612
    head mircea
    7
    5
    3
    1
    bogdan
    radu
    tail 54612
    head mircea
    7
    5
    3
    1
    bogdan
    radu
    tail 54612
    head mircea
    7
    5
    3
    1
    bogdan
    radu
    tail 54612
"""
