# LOGIC:
# ALL A FACTORIAL IS IS (THE NUMBER - 1 )! * THE NUMBER
def factorial(n): 
    # base case
    if n == 1:
        return 1
    # gets the factorial of n-1, multiplies it by n
    else:
        return(factorial(n-1) * n)
print(factorial(2))