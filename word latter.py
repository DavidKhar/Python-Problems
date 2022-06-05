#WORD LATTER:
# YOU ARE GIVEN A STARTING WORD AND AN ENDING WORD.
# YOU ARE ALSO GIVEN A DICTIONARY (NOT A PYTHON DICTIONARY, IT IS A LIST OF WORDS).
# EVERY ADJASCENT PAIR DIFFERS BY ONE SINGLE LETTER.
# they are ALWAYS 3 LETTER WORDS
# their can be duplicate words, to prevent this from mattering i can turn the list of words into a set ( wordset = set(wordList) )

# EXAMPLE:
# startword = hit
# endword = cog
# wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# OUTPUT = SHORTEST SEQUEUNCE LENGTH. THIS WOULD BE 5.

# EXAMPLE 2:
# startword = hit
# endword = cog
# wordList = ["hot","dot","dog","lot","log"]
# if the endword is not in the wordList, return 0.

# PSEUDOCODE
# create a graph (dictionary) using the word list (neighbors are words with one different letter)
# do this by using a nested for loop to compare each word to one another

# after the graph has been made i will run the breadth first search algorithm with it as the graph and the (next line)
# starting word as my starting node. (Instead of printing s i would be adding s to a list and returning the length of that list)

# also i will have a "if the end word is not in the wordlist" statement in the code and if that is true i would return 0

# HOW I AM COMPARING EACH WORD TO KNOW THEY DIFFER BY 1 LETTER TO CREATE THE GRAPH:
# i will use a nested for loop (a for loop inside of a for loop) to create my graph (dictionary) of nodes and neighbors of the word list.
# in the nested for loop to compare each word to the others to tell if they are neighbors I can create a variable (that will reset to 0 at the begining of each run through)
# that is called "differences". This variable will grow by one every time a difference is seen between the two words I am comparing.
# if the number of differences are equal to one, then the words will neighbor eachother. if the differences are > 1, they will not be neighbors.

# TIP:
# create a list of all the different words (in the nested for loop) with a different middle letter, and see if that word is in the word list, if it is, add it to the queue.

wordList = ["POON", "PLEE", "SAME", "POIE", "PLEA", "PLIE", "POIN"]
startword = "TOON"
endword = "PLEA"
# FIX THIS ERROR!!!
# if you cannot get to your endword with the words in the wordlist say somehting
'''
wordList = ["hot", "dot", "dog", "zog", "lot", "sog", "log", "cog", "hup"]
startword = "hit"
endword = "cog"
'''

if endword not in wordList:
    print(0, "(endoword not in wordlist)")
    exit()

#wordList.remove(endword)
#wordList.append(endword)

def makeGraph(wordList):
    if startword not in wordList:
       wordList.insert(0, startword)
    
    graph = {

    }
    
    for i in wordList:
        validNeighbors = []
        for j in wordList:
            differences = 0
            for k in range(len(i)):
                if i[k] != j[k]:
                    differences+=1
            if differences == 1:
                validNeighbors.append(j)
                graph[i] = validNeighbors
    return graph            

queue = []
visited = []
def bfs(visited, queue, node):
    path = []
    queue.append(node)
    visited.append(node)
    while queue:
        s = queue.pop(0)
        path.append(s)
        for neighbor in graph[s]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
          
    i=0
    while i<len(path):

        if i>1:
            
            if path[i] in graph[path[i-2]]:
                path.remove(path[i-1])
        i+=1

    x=len(path)-3
    
    # do what i did above, but see if it is a neighbor of what is ahead by 2 (add 2 to the index)
    while x>=0:
            
        if path[x] in graph[path[x+2]]:
            path.remove(path[x+1])
        x-=1
    if endword not in path:
        print("0 (No path found)")
        exit()
    return (path)
graph = makeGraph(wordList)
path = bfs(visited, queue, startword)
print(len(path))
print(path)

# this is a change