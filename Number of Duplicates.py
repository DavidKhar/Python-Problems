# problem: given a list of numbers, find the number of duplicates for each number
# create a blank empty dictionary
# loop through the numbers list one by one and logic is that: if the number i am looping through is in the dictionary keys,
# (continuation from previous comment) get the value of that key and add one to it. If the number does not exist in the dictionary, add that number as the key & the value as zero

# Homework: Learn all of the methods for dictionaries and ^

x = 0
numbers = [1, 1, 2, 4, 5, 6, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
dictNumbers = {}

# Checking each number's number of duplicates in the list
for number in numbers:
    # if the number is in the dictionary already
    if number in dictNumbers:
        dictNumbers[number] += 1
    else:
        dictNumbers[number] = 1

print(dictNumbers)