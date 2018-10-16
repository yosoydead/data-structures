from myStack import Stk

x = Stk()

x.push(8)
#print(x.peek())
x.push(3)
#print(x.peek())
x.push(6)
x.push(0)
x.push("bogdan")
#print(x.peek())
x.push("radu")

x.push("mircea")
x.iter()
print("top", x.peek())
print("size", x.size())
print("popped",x.pop())
print("top", x.peek())
x.iter()

print("popped", x.pop())
print("top", x.peek())
print("size", x.size())
x.iter()
print("popped", x.pop())
print("top", x.peek())