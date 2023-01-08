# Write a Python program to find the first appearance of the substring 'not'
# and 'poor' from a given string, if 'not' follows the 'poor', replace the
# whole 'not'...'poor' substring with 'good'. Return the resulting string

# I would ask for a test case and get a more in depth understanding of the problem, but my solution will be under these assumptions:
# i will only replace everything inbetween "not" and "poor" (including "not" and "poor") with "good". Also that "not" and "poor"
# may not always be in the string.

class Solution():
    def notPoor(self, string):
        found = False # keeps track of whether or not the string "not"......."poor" has been found
        first = "not" # the first string i am trying to locate
        second = "poor" # the second string i am trying to locate
        next = 0 # count for matches in target and string
        target = first # because first has not yet been found, we are currently trying to match with first
        i=0 # count variable
        while i < len(string):
            setback = -1 # sets the setback to -1 automatically so you move forward by default
            # print(i, next, target, string, target[next], string[i])
            if string[i] == target[next]: # if our current element 
                next +=1 # because a match has been found, we advance by 1 in the target string 
                if next == len(target): # if we have found all of the elements from our current target:
                    if target == first: # if the target is the first one,
                        x = i - len(first) + 1 # i remember this position by making it into a variable
                        target = second # target shiffts to second
                        next = 0 # next resets to 0
                        
                    elif target == second: # if all of the elements in second have been found:
                        found = True # found is true because "not"..."poor"
                        y = i + 1 # saves the position
                        break # breaks the loop
            else: # if it did not match:
                setback = next - 1 # makes it so you will setback in string, to avoid not checking anything
                next = 0 # keeps next at 0/makes next 0 beacuse there is no need to advance
            
            i -= setback # sets back current position in string to make sure that you do not skip over any
        
        if not found: # if "not"..."poor" was not found, i just return the string unchanged
            return string
        return (string.replace(string[x:y], "good", 1)) # replaces the first instance of from not --> poor with good
                    

solution = Solution()
print(solution.notPoor("potatopotatonotnotpoornotpoor"))

# potato potato not not poor not poor

# i do not need a comment for each line, just to make sure that the reader
# understands my code. too many comments is counter productive