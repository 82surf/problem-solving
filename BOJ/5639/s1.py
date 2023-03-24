# 시간초과

import sys
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt')


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def traverse(self):
        if self.left:
            self.left.traverse()
        if self.right:
            self.right.traverse()
        print(self.val)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self.insert_node(self.root, val)

    def insert_node(self, curr, val):
        if val > curr.val:
            if curr.right:
                self.insert_node(curr.right, val)
            else:
                curr.right = Node(val)
        else:
            if curr.left:
                self.insert_node(curr.left, val)
            else:
                curr.left = Node(val)


bst = BST()
for n in sys.stdin:
    bst.insert(int(n))
bst.root.traverse()