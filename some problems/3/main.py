from lst import Lst

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