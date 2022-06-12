# fibonacci sequence
# use recursion
# starts from 0 1 1 2 3 5 8
# the number is the sum of the last two numbers
# 1+2=3, 3+2=5, 5+3==8, etc...
# print everything from 0, to the x index

# the number should always = the last 2 numbers
# does the logic of adding 2 numbers apply to the first two numbers?
# you have to use recursion twice in the same row of code (meaning: You have to call your function twice)
# you will have to use a for loop
# if the number is less than or equal to one: print 0 1

# parameters: fib(5)
# fib(n-1) + fib(n-2)

# when we return, i will be given two of the problems we have previously done, (binary search, palindrome, longest common prefix, etc.)

# HOMEWORK:
# make a while loop, start from 0 untill you hit the index
# always print 0
# have another variable that is 1
# count 1, count 2 & count 3
# 0+1, 1, 1+1, 2, 2+1, 3, 2+3, 5....... untill the index is reached
# use a while loop, and have a counter (define the first two numbers count 1, and count two. count two = 0. count one = 1. also, have another counter/variable 
# which is = count 1 + count 2 -- count 3 [will be stored inside the loop, 1 & 2 are initialized outside of the loop.]) counter/count 0 will run from
# while loop comdition: run from counter variable until it reaches it is less than the last number I want it to be equal to.
# LOGIC: add the two numbers, store it in the sum, then swap the values. Then I will increase the counter until it is no longer lesser than n.


# fib sequence 7 = 0, 1, 1, 2, 3, 5, 8, 13
class Solution:
    def fib(self, n):
        count1=1
        count2=0
        count=0
        print(0)
        while count<n:
            count3=count1+count2
            if count%2 == 0:
                count1 = count3
            else:
                count2 = count3
            print(count3)
            count+=1
solution = Solution()

solution.fib(7)