class Node:
    def __init__(self,data=None):
        self.data=data
        self.left = None
        self.right = None
class bst:
    def __init__(self):
        self.root = None
    def append(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                if data > cur.data:
                    if cur.right == None:
                        cur.right = Node(data)
                        break
                    else:
                        cur = cur.right
                elif data < cur.data:
                    if cur.left == None:
                        cur.left = Node(data)
                        break
                    else: 
                        cur = cur.left
                else: 
                    print('Error: value in tree!')
                    break
    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
    def _print_tree(self,cur):
        if cur != None:
            self._print_tree(cur.left)
            print(str(cur.data))
            self._print_tree(cur.right)
import random

binary = bst()
for i in range(100):
    binary.append(random.randint(1,1000))
binary.print_tree()

