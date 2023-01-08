# Write a function max_sum_path(triangle: List[List[int]]) -> int 
# that takes in a triangle of numbers as a list of lists,
# and returns the maximum sum that can be obtained by
# starting at the top of the triangle and moving down to an adjacent
# number on the row below. You can only move to the
# number on the row below that is directly below the number you are currently on.

# test case: [[1], [2, 1], [1, 2, 3], [1, 2, 3, 4]]
#     1
#    2 1
#   1 2 3
#  1 2 3 4
# return 5
# all positive intergers in the triangle, nothing weird

# HINTS:
# USE RECURRSION.
# GET THE MAXIMUM EVERY TIME BY PASSING THE NEXT LIST/NUMBER, TRY TO GET THE MAXIMUM VALUE BETWEEN THE NEXT TWO NUMBERS.


# pseudocode:
# TO SEE IF TWO ELEMENTS ARE ADJECENT i have to see the index of the one that i chose above,
# and get that same index and that index + 1 are my next possible choices.
#
# i can use reccurrsion to go down each path, and if that path beat my previous best amount i
# can replace that best with the path i just went down. i can check if each element is valid
# for being the next element by if its index is = the last decisions index, or that + 1. i can
# keep track of all of my choices in an array, and keep track of the bests in an array as well.
# i need a base case, and the base case could be that if the 

class Solution:
    def max_sum_path(self, triangle):
        '''
        # base cases:
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        # recursion part
        else:
            # i think that i can call this function on the left adjacent element
            # and on the right adjacent element of the current element, and then keep
            # on doing that and when i reach the bottom i can compare between the previous 
            sum = triangle[0][0]
            max_sum_path(triangle[1:]) # chops the first element off
        '''
        paths = {

        }
        while len(triangle) > 1:
            last = len(triangle)-1
            for i in range(len(triangle[last-1])):
                #print(i)
                for j in triangle:
                    print(j)
                triangle[last-1][i] += max(triangle[last][i], triangle[last][i + 1])
            triangle = triangle[:-1]
        return triangle
triangle = [[1], [2, 1], [1, 2, 3], [1, 2, 3, 4]]
solution = Solution()
print(solution.max_sum_path(triangle))

# solve this NO HELP!
# play with some examples and numbers
# create a class where i can do examples and test things
# upload thsese to github!!
'''numbers = ['1', '2', '3', '4']
print(len(numbers))'''
'''numbers = ['1', '2', '3', '4']
print(numbers)
numbers = numbers[:-1]
print(numbers)'''