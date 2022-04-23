# make one with two players and no computers
import random
class Game:
    def countGameVsComputer(self):
        # you can make the gamelist by doing a for loop (for i in range(21))
        gameList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18' , '19', '20', '21']
        x=random.randint(1, 2)
        firstMove = True
        while gameList:
            #print("Current remaining numbers:", gameList)
            computerMove = []
            if x % 2 == 0:
                if firstMove:
                    
                    temp = random.randint(1,3)
                    for i in range(temp):
                        j = gameList.pop(0)
                        computerMove.append(j)
                    print("Computer move:", computerMove)
                    x+=1
                    continue
                moveLen = 4 - len(playerMove)                
                for i in range(moveLen):
                    if len(gameList) == 0:
                        lastMove = "computer"
                        break
                    y = gameList.pop(0)
                    computerMove.append(y)
                lastMove = "computer"
                print("Computer move:", computerMove)
            else:
                playerMove = input("Enter your move: ")
                if "," in playerMove:                    
                    playerMove = playerMove.split(', ')
                else:
                    playerMove = playerMove.split(" ")
                for i in playerMove:
                    if i in gameList:
                        gameList.remove(i)
                lastMove = "player"
            firstMove = False
            x+=1
        
        if lastMove == "player":
            print("You lose! I win!")
        elif lastMove == "computer":
            print("Good job! You win!")
    def countGameVsPlayer(self):
        x=random.randint(1,2)
        gameList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18' , '19', '20', '21']
        while gameList:
            
            print("Current remaining moves/numbers:", gameList)
            if x%2 == 0:
                playerMove = input("Enter your move player 1: ")
                if "," in playerMove:                    
                    playerMove = playerMove.split(', ')
                else:
                    playerMove = playerMove.split(" ")
                for i in playerMove:
                    if i in gameList:
                        gameList.remove(i)
                lastMove = "player1"
            elif x%2 != 0:
                playerMove = input("Enter your move player 2: ")
                if "," in playerMove:                    
                    playerMove = playerMove.split(', ')
                else:
                    playerMove = playerMove.split(" ")
                for i in playerMove:
                    if i in gameList:
                        gameList.remove(i)
                lastMove = "player2"
        
            x+=1
        if lastMove == "player2":
            print("Player one wins!")
        elif lastMove == "player1":
            print("Player two wins!")
    def playCountGame(self):
        mode = input("would you like to play against a friend or against the computer? ")
        if mode == "friend":
            self.countGameVsPlayer()
        elif mode == "computer":
            self.countGameVsComputer()
print("\n\n\n\n\n\n\n\n")
play = Game()
play.playCountGame() 