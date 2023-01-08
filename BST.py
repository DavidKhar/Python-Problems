# HOMEWORK:

# Write a Python program to create a Balanced Binary Search Tree (BST) using an array (given) elements where array elements are sorted in ascending order.
# the array is always sorted !
# find the root, give the left array, give the right array.
# [1,2,3,4,5,6,7]
# [4] root node (middle)
# find the left and right of that node, 3, (1 level deeper)
#
# to get the left node, you have to give the
# start to the middle of the array.
# to get the right node, you have to pass
#  the middle + 1 until the end

# initially i will pass the whole array. when i recall the function
# i will be passing it on either the left or the right half of the array

# everytime i pass that array i find out the middle, create that node, and do the left/right,
# until my array is empty

# syntax :
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedBST(arr):
    # base condition
    if not arr:
        return None
    # find the middle element of arr
    mid = len(arr)//2
    node = TreeNode(arr[mid])
    node.left = sortedBST(arr[:mid])  # left array (recursion)
    node.right = sortedBST(arr[mid+1:])  # right array (recursion)
    return node

def preOrder(node):
        if not node:
            return
        print(node.val)
        preOrder(node.left)
        preOrder(node.right)


result = sortedBST([1, 2, 3, 4, 5, 6, 7])
print(result)
preOrder(result)


# you have to find the middle of the array each time, everything to the left of
# that middle element is the left array, and everything to the right of that is
# part of the right array. if there is only one element in the array, print that single
# element. call reccurssively on the left half of the array, and add the right half to the stack
# by having that after the left, so that the right array is added to the stack. you print the nodes of
# the binary search tree,
