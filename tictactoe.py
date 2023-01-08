import random
def winCheck(BOARD): # 0 IF NO WINNER, 1 IF PLAYER WINNER, 2 IF CMOPUTER WINNER
    if BOARD[0] == BOARD[1] and BOARD[0] == BOARD[2]: 
        if BOARD[0] == "X":
            return 1
        else:
            return 2
        
    elif BOARD[3] == BOARD[4] and BOARD[3] == BOARD[5]: 
        if BOARD[3] == "X":
            return 1
        else:
            return 2

    elif BOARD[6] == BOARD[7] and BOARD[6] == BOARD[8]: 
        if BOARD[6] == "X":
            return 1
        else:
            return 2

    elif BOARD[0] == BOARD[3] and BOARD[0] == BOARD[6]: 
        if BOARD[0] == "X":
            return 1
        else:
            return 2
    
    elif BOARD[1] == BOARD[4] and BOARD[1] == BOARD[7]: 
        if BOARD[1] == "X":
            return 1
        else:
            return 2

    elif BOARD[2] == BOARD[5] and BOARD[2] == BOARD[8]: 
        if BOARD[2] == "X":
            return 1
        else:
            return 2

    elif BOARD[0] == BOARD[4] and BOARD[0] == BOARD[8]: 
        if BOARD[0] == "X":
            return 1
        else:
            return 2
    elif BOARD[2] == BOARD[4] and BOARD[2] == BOARD[6]:
        '''BOARD[2] = "-"
        BOARD[4] = "-"
        BOARD[6] = "-"'''
        if BOARD[0] == "X":
            return 1
        else:
            return 2
    else:
        return 0

def tictactoe():
    turnkeeper = random.randint(0, 1)
    board1 = ["1", "2", "3"]
    board2 = ["4", "5", "6"]
    board3 = ["7", "8", "9"]
    BOARD = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    available = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while len(available)>0:
        print("\n")
        print(board1)
        print(board2)
        print(board3)
        print("\n")
        if turnkeeper%2 == 0: # IF IT IS THE USERS TURN:

            userChoice = input("Where would you like to go? ") # MAKING THE USER CHOOSE A VALID TURN
            if userChoice not in available:
                while userChoice not in available:
                    print(board1)
                    print(board2)
                    print(board3)
                    userChoice = input("That square is not available, please move somewhere else! ")
            available.remove(userChoice)
            BOARD[int(userChoice)-1] =  "X"
            if int(userChoice) <=3:
                board1[int(userChoice)-1] = "X"
            elif int(userChoice) <= 6:
                board2[int(userChoice)-4] = "X"
            else:
                board3[int(userChoice)-7] = "X"
            
            
            
        
        else: # IF IT IS THE COMPUTERS TURN:
            computerChoice = available[random.randint(0, len(available)-1)]
            available.remove(computerChoice)
            BOARD[int(computerChoice)-1] =  "O"
            if int(computerChoice) <=3:
                board1[int(computerChoice)-1] = "O"
            elif int(computerChoice) <= 6:
                board2[int(computerChoice)-4] = "O"
            else:
                board3[int(computerChoice)-7] = "O"
            
        # CHECKS IF SOMEONE HAS WON:
        winner = winCheck(BOARD)
        if winCheck(BOARD) == 0:
            pass
        elif winner == 1:
            print(board1)
            print(board2)
            print(board3)

            print("You win!")
            return("win")
        elif winner == 2:
            print(board1)
            print(board2)
            print(board3)

            print("You lose!")
            return("lose")

        turnkeeper+=1
        
tictactoe()
