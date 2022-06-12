import math
class Solution:
    def population(self, startingNum, annualGrowth, years):
        #recursive method:
        """
        if years == 1:
            return(math.floor(annualGrowth * startingNum))
        else:
            return(math.floor(self.population(startingNum, annualGrowth, years-1) * annualGrowth))
        """
        #for loop method:
        for i in range(years):
            startingNum = math.floor(startingNum * annualGrowth)
        return startingNum

    def money(self, startingNum, annualGrowth, years):
        # recursive method:
        """
        if years == 1:
            return(startingNum * annualGrowth)
        else:
            return(self.population(startingNum, annualGrowth, years-1) * annualGrowth)
        """
        #for loop method:

        for i in range(years):
            startingNum*=annualGrowth
        return startingNum
        
solution = Solution()
print(solution.population(1000, 1.2, 5))