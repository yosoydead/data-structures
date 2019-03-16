class MyHashTable:
    #initialize the hash table so it will have an array of a certain length
    def __init__(self, size = 17):
        self.keyMap = [None] * size

    #hash functions have alot of things to do with prime numbers
    #prime numbers determine how many collisions of an item being already in the collection
    #also, this hash table and hash function will work only with strings at the moment
    def hash(self, key):
        total  = 0
        weirdPrime = 31

        for i in range( min(len(key), 100 ) ):
            #grab the current character of the input string
            char = key[i]

            #grab the characters ascii code
            #convert the char to its position in the alphabet
            position = ord(char) - 96

            #the hash calculation will be based on the alphabet position of the characters
            #the chosen prime number
            #eveything modulo the length of the classes array
            total = (total * weirdPrime + position) % len(self.keyMap)
        
        #return the hash
        return total

    #set function
    #hashes the key
    #stores the key-value pair in the hash table array via separate chaining
    #separate chaining means that if there is an item at the given key, 
    #create a collection to store items that have the same key
    def st(self, key, value):
        index = self.hash(key)

        #because i initialize everything in the array with None
        #i have to clear that first
        if self.keyMap[index] == None:
            #set the current index to be an empty array
            self.keyMap[index] = []
            #self.keyMap[index].append([key, value])

        #if the index is not None, then push the new key-value pair into the array
        self.keyMap[index].append([key, value])


    #get function
    #hashes the key
    #retrieves the key-value pair in the hash table
    #if the key isnt found, return undefined
    def get(self, key):
        index = self.hash(key)

        #check to see if there is something at that index
        if self.keyMap[index]:
            #loop over all the elements in the nested array
            for i in range(0, len(self.keyMap[index])):
                #if the first index of that nested array is == to the key
                if self.keyMap[index][i][0] == key:
                    #return its value
                    return self.keyMap[index][i][1]

    #loop through the hash table array ad return an array of keys in the table
    def keys(self):
        keys = []

        for i in range(0, len(self.keyMap)):
            #if there is something at that index
            if self.keyMap[i]:
                for j in range(0, len(self.keyMap[i])):
                    #dont add duplicate keys
                    if not keys.__contains__(self.keyMap[i][j][0]):
                        #append the key of every key-value pairs
                        keys.append(self.keyMap[i][j][0])

        return keys

    #loop through the hash table array ad return an array of values in the table
    def values(self):
        values = []

        for i in range(0, len(self.keyMap)):
            #if there is something at that index
            if self.keyMap[i]:
                for j in range(0, len(self.keyMap[i])):
                    #dont add duplicate values
                    if not values.__contains__(self.keyMap[i][j][1]):
                        #append the value of every key-value pairs
                        values.append(self.keyMap[i][j][1])

        return values



