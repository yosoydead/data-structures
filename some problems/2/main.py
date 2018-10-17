from lst import Lst

myFile = open(r"D:\visual studio exercises\data structures\some problems\2\numbers.txt", "r")
string = ""
for line in myFile:
    string = line

string = string.split(" ")

x = Lst()
x.populate(string)
x.iter()