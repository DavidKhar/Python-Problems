# Write a Python program to find  the greatest common divisor (gcd) of two integers
import math
class Solution:
    def findGCD(self, num1, num2):
        less = min(num1, num2)
        more = max(num1, num2)
        gcf = 0
        count = less
        while count > 0:
            if math.floor(less/count) == less/count and math.floor(more/count) == more/count:
                return count
            count-=1
        return gcf
        '''
         # make this one work as homework!!!
    def findGCDReccursive(self, num1, num2):
        low = min(num1, num2)
        high = max(num1, num2)
        if low == 0:
            return high
        if low == 1:
            return 1
        return(self.findGCDReccursive(low, high % low))
        '''
    # next time: write comments!
    def findGCDReccursive(self, num1, num2):
        low = min(num1, num2) # low = lesser of num1 and num2
        high = max(num1, num2) # high = greater of num1 and num2
        if low == 0: # if low = 0, the function will not advance any further so this is a base case
            return high
        if low == 1: # if low = 1, the function will not advance any further so this is a base case
            return 1
        return(self.findGCDReccursive(low, high%low)) # runs the findGCDReccursive function reccursively with the
        # same low, but the high changes to the remainder of high/low
        

        # pseudocode:
        # 
        


# should have clarified whole numbers only!!!
solution = Solution()
print(solution.findGCD(50, 12))
print(solution.findGCDReccursive(12, 50))


# HINT ON HOW TO BETTER SOLVE IT:
# 1. USE MIN/MAX FUNCTION. (AT THE TOP)  -- checked off
# 2. USE THE OPERATOR CALLED modulo %, GIVES REMAINDER OF THE TWO NUMBERS
# 3. USE RECURRSION
# 4. GIVE THE REMAINDER EVERY TIME YOU DO RECCURSION, OUTPUT = MODULO % AND GIVE IT BACK TO THE RECCURSIVE CALL,
# REASON = YOU MUST ALWAYS GET TO THE GREATEST COMMON DIVISOR
# REMEMBER YOUR BASE CASE!

# [10, 12]: --> 2, 1
# [10, 20]  --> 10

# LOGIC:
