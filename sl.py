import random

class Node:
    def __init__(self, level, key, value):
        self.key = key
        self.value = value
        # Pointers to nodes of different levels
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_lvl, P):
        # max level of the skip list
        self.MAX_LVL = max_lvl
        
        self.P = P
        self.header = self.create_node(self.MAX_LVL, None, None)
        # Current level of skip list
        self.level = 0

    def create_node(self, lvl, key, value):
        return Node(lvl, key, value)

    def random_level(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAX_LVL:
            lvl += 1
        return lvl

    def insert(self, key, value):
        update = [None] * (self.MAX_LVL + 1)
        current = self.header

        # Start from the highest level of skip list and move downwards
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        # Reached level 0 and move to the right, which is the desired position
        current = current.forward[0]

        # If current is None or current's key is not equal to key,
        # then we insert node between update[0] and current node
        if current is None or current.key != key:
            # Generate a random level for node
            rlevel = self.random_level()

            # If random level is greater than list's current
            # level (node with highest level inserted in 
            # list so far), initialize update value with reference to header
            if rlevel > self.level:
                for i in range(self.level + 1, rlevel + 1):
                    update[i] = self.header
                # Update the list current level
                self.level = rlevel

            # Create new node with random level generated
            n = self.create_node(rlevel, key, value)

            # Insert node by rearranging references 
            for i in range(rlevel + 1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n

    def search(self, key):
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        # Reached level 0 and advance to the right, which is possibly our desired node
        current = current.forward[0]

        # If current node have key equal to searched key, we found it
        if current and current.key == key:
            return current.value
        return None

    def display_list(self):
        print("\n*****Skip List*****")
        for i in range(self.level + 1):
            print("Level {}: ".format(i), end=" ")
            node = self.header.forward[i]
            while node != None:
                print(node.key, end=" ")
                node = node.forward[i]
            print("")
