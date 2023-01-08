class Solution:
    def reverseAString(self, string):
        # HOMEWORK: TRY USING RECURSION TO SOLVE THIS PROBLEM !!!!
        #return string[::-1]
        print(string)

        if len(string) == 1: # if there is only one character remaining, it just puts out that character
            return string
        # returns the last character plus the reversed version of the rest of it
        return string[-1] + self.reverseAString(string[0:-1])

solution = Solution()
print(solution.reverseAString("Apple"))