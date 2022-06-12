usersNumbers = []
numbersDict = {}

# getting the userNumber's items
while 1==1:
    number = input("What number would you like to add to the list (Type \"Done\" to move on)\n")
    if number == "done" or number == "Done":
        break
    else:
        number = float(number)
        usersNumbers.append(number)
    
# defining the functions
def findDuplicates(numbers):
    for number in numbers:
    # if the number is in the dictionary already
        if number in numbersDict:
            numbersDict[number] += 1
        else:
            numbersDict[number] = 1
    return(numbersDict)


def findAverage(numbers):
    return(sum(numbers) / len(numbers))



duplicates = findDuplicates(usersNumbers)
average = findAverage(usersNumbers)
    

print("The numbers of duplicates for each item in your list are:", duplicates)
print("The average of the numbers you entered are:", average)
