from hashTable import MyHashTable

ht = MyHashTable(4)
ht.st("maroon", "#800000")
ht.st("yellow", "#ffff00")
ht.st("olive", "#808000")
ht.st("salmon", "#fa8072")
ht.st("lightcoral", "#f08080")
ht.st("mediumvioletred", "#c71585")
ht.st("plum", "#dda0dd")
ht.st("purple", "#dda0dd")
ht.st("violet", "#dda0dd")
ht.st("fucsia", "#dda0dd")
ht.st("are we done?", "yes")
print((ht.keyMap))

print(ht.get("maroon"))
print(ht.get("are we done?"))
print(ht.keys())
