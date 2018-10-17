from lst import Lst
import os

even = Lst()
odd = Lst()

myFile = open(r"D:\visual studio exercises\data structures\some problems\3\numbers.txt", 'r')

string = ""
for item in myFile:
    string = item

string = string.split(" ")

for item in string:
    if int(item) % 2 == 0:
        even.add(int(item))
    else:
        odd.add(int(item))

even.iter()
print("-------------------------")
odd.iter()

#this is the path where the main file is located
# __file__ means the file that is executed
currentPath = os.path.dirname(os.path.relpath(__file__))
string1 = even.listToString()
string2 = odd.listToString()

with open(os.path.join(currentPath, "output.txt"), "w") as file:
    file.write(string1.strip() + "\n")
    file.write(string2.strip())

