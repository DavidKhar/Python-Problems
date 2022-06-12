def isPalindrome(word):
    x = -1
    y = 0
    list = []
    for i in str(word):
        x+=1
        list.append(i)
    while True:
        if list[y]!=list[x]:
            return False
        y+=1
        x-=1
        if x<y:
            return True

    # this also works but is worse practice
    """
    return(word[::-1] == word)
    """
    
print(isPalindrome(input("Input a string to be checked as a palindrome: ")))