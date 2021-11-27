class Board:
    def __init__(self,size):
        self.size = size 
        self.grid = []
        self.end = False

        for x in range(self.size):
            row = []
            for y in range(self.size):
                row.append('-')
            self.grid.append(row)
        
    def printBoard(self):

        for row in range(self.size):
            print(" ".join(self.grid[row]))

        


