import statistics


class Node:
    def __init__(self, data, color="red"):
        self.data = data
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0, "black")  # Null nodes are black
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.steps = []
        self.rotations = []

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = "red"  # New nodes are red

        parent = None
        current = self.root

        curSteps = 0

        while current != self.TNULL:
            parent = current
            if node.data < current.data:
                current = current.left
            else:
                current = current.right
            curSteps += 1

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

        if node.parent is None:
            node.color = "black"
            self.steps.append(curSteps)
            self.rotations.append(0)
            return

        if node.parent.parent is None:
            self.steps.append(curSteps)
            self.rotations.append(0)
            return

        # Fix the tree
        self.steps.append(curSteps)
        # rotations are added in the fix_insert method
        self.fix_insert(node)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        curRotations = 0

        while k.parent.color == "red":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # left uncle
                if u.color == "red": #red uncle
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:  # black uncle
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                        curRotations += 1
                    
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.left_rotate(k.parent.parent)
                    curRotations += 1
            else:  # Mirror case: Parent is the left child of its parent
                u = k.parent.parent.right  # right uncle

                if u.color == "red":  # red uncle
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:  # black uncle
                    if k == k.parent.right: 
                        k = k.parent
                        self.left_rotate(k)
                        curRotations += 1
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.right_rotate(k.parent.parent)
                    curRotations += 1

            if k == self.root:
                break
        self.rotations.append(curRotations)
        self.root.color = "black"

    def count_leaves(self, node):
        
        if node == self.TNULL:
            return 0
        
        if node.left == self.TNULL and node.right == self.TNULL:
            return 1
        
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    def get_number_of_leaves(self):
        return self.count_leaves(self.root)

    def compute_height(self, node):
        if node == self.TNULL:
            return 0
        else:
            left_height = self.compute_height(node.left)
            right_height = self.compute_height(node.right)
            return max(left_height, right_height) + 1

    def get_tree_height(self):
        return self.compute_height(self.root)

    def printStatistics(self):
        print("Red Black Tree")
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

        print("Height of the tree: ", self.get_tree_height())
        print("number of leaves: ", self.get_number_of_leaves())
        print("")