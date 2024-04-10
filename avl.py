import statistics


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
        self.steps = []
        self.rotations = []

    def insert(self, key):
        if not self.root:
            self.steps.append(0)
            self.root = Node(key)
        else:
            self.root, steps, rotations = self._insert(self.root, key, 0, 0)
            self.steps.append(steps)  # Append steps taken for this insertion
            self.rotations.append(rotations)  # Append rotations taken for this insertion

    def _insert(self, root, key, steps=0, rotations=0):
        if not root:
            return Node(key), steps, rotations
        elif key < root.key:
            root.left, steps, rotations = self._insert(root.left, key, steps+1, rotations)
        else:
            root.right, steps, rotations = self._insert(root.right, key, steps+1, rotations)

        # Update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left), 
                              self.getHeight(root.right))

        # balance the tree after insertion
        balance = self.getBalance(root)

        if balance > 1 and key < root.left.key:
            return self.rightRotate(root), steps, rotations+1

        if balance < -1 and key > root.right.key:
            return self.leftRotate(root), steps, rotations+1

        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root), steps, rotations+1

        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root), steps, rotations+1

        if root == self.root:
            self.steps.append(steps)

        return root, steps, rotations

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return x

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root=None):
        if root is None:
            root = self.root
        if root is not None:
            print("{0} ".format(root.key), end="")
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def count_leaves(self, node):
        # If the tree is empty, return 0
        if not node:
            return 0
        # If the node is a leaf node
        if not node.left and not node.right:
            return 1
        # Recursively count the leaves in both the left and right subtree
        return self.count_leaves(node.left) + self.count_leaves(node.right)


    def printStatistics(self):
        print("AVL Tree")
        print("Steps:")
        print("minimum: ", min(self.steps))
        print("maximum: ", max(self.steps))
        print("mean", sum(self.steps) / len(self.steps))
        print("standard deviation: ", statistics.stdev(self.steps))
        print("median: ", self.steps[len(self.steps) // 2])

        print("Rotations:")
        print("minimum: ", min(self.rotations))
        print("maximum: ", max(self.rotations))
        print("mean", sum(self.rotations) / len(self.rotations))
        print("standard deviation: ", statistics.stdev(self.rotations))
        print("median: ", self.rotations[len(self.rotations) // 2])

        print("Height of the tree: ", self.root.height)
        print("number of leaves: ", self.count_leaves(self.root))
        print("")