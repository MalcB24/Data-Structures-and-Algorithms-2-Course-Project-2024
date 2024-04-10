# Create an array of 5,000 integers whose values start at 1 and end at
# 5,000

arr = [0] * 5000
for i in range(0, 5000):
    arr[i] = i + 1

# Implement the Knuth shuffle algorithm to randomise the order of the
# elements in the array. The implementation should yours; don’t use any
# inbuilt array shuffling function from your programming language. 

import random
def knuth_shuffle(arr):
    n = len(arr)
    for i in range(n-1, 0, -1): 
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = knuth_shuffle(arr)

# Insert all the 5,000 integers from the array into an AVL tree, a RedBlack tree, and a Skip List. The implementations of these three data
# structures should be your own.

import avl
import rbt
import sl

avl_tree = avl.AVLTree()
rb_tree = rbt.RedBlackTree()
sl = sl.SkipList(5, 0.5)

for i in range(0, 5000):
    avl_tree.insert(arr[i])
    rb_tree.insert(arr[i])
    sl.insert(arr[i], arr[i])

# Create another array containing 1,000 random integers in the range
# [0…100,000]. This array may contain duplicates.

arr = [0] * 1000


for i in range(0, 1000):
    arr[i] = random.randint(0, 100000)

# Insert all the elements from this second array into the AVL tree. When
# inserting, keep track of statistics
avl_2 = avl.AVLTree()
rbt_2 = rbt.RedBlackTree()

for i in arr:
    avl_2.insert(i)
    rbt_2.insert(i)

# Print the statistics
rbt_2.printStatistics()