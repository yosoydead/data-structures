from lst import SLL
import random

lst = SLL()
def populate():
    for i in range(0, 11):
        x = random.randint(1, 9)
        lst.add(x)

populate()
string = lst.concatinate()
print(string)