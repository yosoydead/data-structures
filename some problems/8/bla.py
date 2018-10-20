from lst import SLL
import random
x = SLL()
def palindrom(string):
    low = 0
    high = len(string)-1

    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True

def populate(lst, string):
    # for i in range(0, 10):
    #     char = random.randint(97, 122)
    #     lst.add(chr(char))
    for item in string:
        lst.add(item)

populate(x, "abbc")
string = x.returnStringFromList()
print(palindrom(string))