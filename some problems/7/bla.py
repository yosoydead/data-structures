from lst import SLL
import random
matrix = []

m = 5
n = 7

for i in range(0, 5):
    new = []
    for j in range(0,7):
        x = random.randint(1, 15)
        new.append(x)
    matrix.append(new)
    new = []

def createLLS(matrix):
    storedLLS = []

    for i in range(0, len(matrix)):
        new = SLL()
        for j in range(0, len(matrix[i])):
            new.add(matrix[i][j])
        storedLLS.append(new)
        new = SLL()
    return storedLLS

x = createLLS(matrix)

for item in x:
    item.iter()
    print("\n-------------------------")



