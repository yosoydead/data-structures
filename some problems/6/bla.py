from sll import SLL
import random

x = SLL()
y = SLL()

def concat(lst1, lst2):
    new = SLL()
    
    head = lst1.head
    while head != None:
        new.add(head.data)
        head = head.next

    head = lst2.head
    while head != None:
        new.add(head.data)
        head = head.next
    
    return new
    
x.populate(5)
y.populate(5)

z = concat(x,y)
z.iter()