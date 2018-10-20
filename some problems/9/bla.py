from ll import CLL

x = CLL()
x.add(1)
x.add(2)
x.add(3)
x.add(4)
# print("head",x.head.data, "tail", x.tail.data)
# head = x.removeHead()
# x.add(head)
# print("head",x.head.data, "tail", x.tail.data)
# bla = x.concat()
initial = x.concat()
print(initial)
nextVal = ""
while nextVal != initial:
    head = x.removeHead()
    x.add(head)
    nextVal = x.concat()
    print(nextVal)
