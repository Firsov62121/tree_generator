#! /usr/bin/python3
import numpy as np

class Node:
    ids = []
    idNum = 0

    def setIDs(maxsize):
        Node.ids = np.empty(maxsize - 1, dtype=int)
        for i in range(1, maxsize):
            Node.ids[i - 1] = i
        np.random.shuffle(Node.ids)
        Node.idNum = 0

    def getID():
        res = Node.ids[Node.idNum]
        Node.idNum += 1
        return res

def createTree(filename, n, depth):
    if n != 1:
        maxsize = (n ** depth - 1) // (n - 1)
    else:
        maxsize = depth
    print("maxsize =", maxsize)
    if input("continue? (yes or no)") == 'no':
        return
    Node.setIDs(maxsize)
    print("id setted")
    prevNodes = np.array([0])
    res = np.empty([maxsize - 1, 2], dtype=int)
    resPos = 0
    for de in range(depth - 1):
        print(f"depth = {de + 1}")
        newPrev = np.empty(prevNodes.size * n, dtype=int)
        newPrevPos = 0
        for node in prevNodes:
            for __ in range(n):
                id = Node.getID()
                newPrev[newPrevPos] = id
                newPrevPos += 1
                res[resPos][0] = node
                res[resPos][1] = id
                resPos += 1
        del prevNodes
        prevNodes = newPrev
    print("shuffle edges")
    np.random.shuffle(res)
    print("writing tree into file")
    with open(filename, 'w+') as file:
        file.write(f"{maxsize - 1}\n")
        for j in range(maxsize - 1):
            file.write(f"{res[j][0]}\t{res[j][1]}\n")


n = int(input("children count = "))
h = int(input("height = "))
filename = input("filename = ")
createTree(filename, n, h)
