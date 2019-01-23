from node import Node
class BST:
    #constructor for the tree
    #when created, the root node is null
    #every node from the root has to have a left and a right pointer
    #which will be branches/children
    def __init__(self):
        self.root = None

    #method that searches the tree to see if a specific value is in the tree
    def contains(self, value):
        #start at the root
        #if there is no root, return null
        if self.root == None:
            return False

        #if there is a root, check if the value of the node is the one we are looking for
            #if it is, stop
        current = self.root
        found = False

        while current and (not found):
            #if not, check if the value is < or > than the value of the root
                #if >
                    #check to see if there is something to the right
                        #if it is, move to that node and repeat steps
                        #if not, stop
            if value < current.data:
                current = current.left
                #if <
                    #check to see if there is something to the left
                        #if it is, move to that node and repeat steps
                        #if not, stop
            elif value > current.data:
                current = current.right
            #if we found, return
            else:
                return True

        return False


    #method to insert into the tree
    def insert(self, data):
        #create a new node
        newNode = Node(data)
        #start from the root

        #check if there is a root
            #if not, the new node becomes the root
        if self.root == None:
            self.root = newNode
        else:
        #if there is a root
            #check if the value of the new node is < or > than the root
            current = self.root

            while True:
                #if the newNode data is already in the tree
                if data == current.data:
                    return None
            #if it is >
                #check to see if there is a node to the right
                    #if there is, move to that node and repeat the steps
                    #if not, add the new node as the right property
                if data < current.data:
                    if current.left == None:
                        current.left = newNode
                        return
                    else:
                        current = current.left
            #if it is <
                #check to see if there is a node to the left
                    #if there is, move to that node and repeat the steps
                    #if not, add the new node as the left property
                elif data > current.data:
                    if current.right == None:
                        current.right = newNode
                        return
                    else:
                        current = current.right

    