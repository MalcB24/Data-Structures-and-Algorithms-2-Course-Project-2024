import random
import statistics

class Node:
    def __init__(self, level, key, value):
        self.key = key
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_lvl, P):
        self.MAX_LVL = max_lvl
        self.P = P
        self.header = self.create_node(self.MAX_LVL, None, None)
        self.level = 0
        self.steps = []  # List to track the number of steps to insertion point
        self.promotions = []  # List to track promotions

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
        step_count = 0  # Initialize step count for this insertion

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
                step_count += 1  # Increment step count for each node traversed
            update[i] = current

        current = current.forward[0]

        if current is None or current.key != key:
            rlevel = self.random_level()
            if rlevel > self.level:
                for i in range(self.level + 1, rlevel + 1):
                    update[i] = self.header
                self.level = rlevel

            n = self.create_node(rlevel, key, value)
            promotions_this_time = rlevel + 1  # Record the number of levels the node is inserted into

            for i in range(rlevel + 1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n

            self.steps.append(step_count)  # Record steps for this insertion
            self.promotions.append(promotions_this_time)  # Record promotions for this insertion

    def reset_stats(self):
        self.steps = []
        self.promotions = []

    def printStatistics(self):
        print("Skip List Statistics")
        print("Steps to Insertion Point:")
        print("Minimum: ", min(self.steps))
        print("Maximum: ", max(self.steps))
        print("Mean: ", sum(self.steps) / len(self.steps))
        print("Standard Deviation: ", statistics.stdev(self.steps))
        print("Median: ", statistics.median(self.steps))
        print("Promotions:")
        print("Minimum: ", min(self.promotions))
        print("Maximum: ", max(self.promotions))
        print("Mean: ", sum(self.promotions) / len(self.promotions))
        print("Standard Deviation: ", statistics.stdev(self.promotions))
        print("Median: ", statistics.median(self.promotions))
        print("Current Max Level: ", self.level)