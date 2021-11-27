from player import Player 
from board import Board

turn = [0]

def findWinner(currSymbol,currBoard):

    # check all the rows
    for row in range(len(currBoard.grid)):
        if currBoard.grid[row][0] == currBoard.grid[row][1] == currBoard.grid[row][2] and currBoard.grid[row][0] != '-':
            return True
    
    # check all the cols
    for col in range(len(currBoard.grid[0])):
        if currBoard.grid[0][col] == currBoard.grid[1][col] == currBoard.grid[2][col] and currBoard.grid[0][col] != '-':
            return True 
        
    # checking both the diagonals 
    if currBoard.grid[0][0] == currBoard.grid[1][1] == currBoard.grid[2][2] and currBoard.grid[0][0] != '-':
        return True
    

    if currBoard.grid[0][2] == currBoard.grid[1][1] == currBoard.grid[2][0] and currBoard.grid[0][2] != '-':
        return True 
    
    return False 

def play(i,j,player1,player2,currBoard,turn):

    i -= 1
    j -= 1
    
    if i < 0 or j < 0 or i >= 3 or j >= 3 or currBoard.grid[i][j] != '-' or currBoard.end == True:
        print("invalid move")
        return 
    
    if turn[0] % 2 == 0:
        currBoard.grid[i][j] = player1.symbol 
        
        if findWinner(player1.symbol,currBoard) == True:
            print(player1.name,"won the match")
            currBoard.end = True
            
        currBoard.printBoard()
    
    else:
        currBoard.grid[i][j] = player2.symbol 

        if findWinner(player2.symbol,currBoard) == True:
            print(player2.name,"won the match")
            currBoard.end = True

        currBoard.printBoard()
    
    turn[0] += 1


currBoard = Board(3)

# first lets make the players
symbol,name = input().split()
player1 = Player(symbol,name)

symbol,name = input().split()
player2 = Player(symbol,name)

currBoard.printBoard()

while True:
    str1 = input()
    if str1 == "exit":
        break 

    i,j = map(int,str1.split())
    print("===============================================")
    play(i,j,player1,player2,currBoard,turn)

