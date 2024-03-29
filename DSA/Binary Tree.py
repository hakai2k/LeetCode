class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insertData(self, data):
        if self.data:
            if self.data:
                if data < self.data:
                    if self.left is None:
                        self.left = Node(data)
                    else:
                        self.left.insertData(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insertData(data)
        else:
            self.data = data
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()

root = Node(10)

root.insertData(12)
root.insertData(7)
root.insertData(23)

root.printTree()