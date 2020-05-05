
class Grid():
    MAX_ROWS = 5
    MAX_COLS = 6
    def __init__(self):
        self.cells = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]]

    def showGrid(self):
        for r in range(len(self.cells)):
            print(" " + str(r + 1) + " " + str(self.cells[r]))
        print("\n    1, 2, 3, 4, 5, 6, 7 ")

    def addChip(self, player, col):
        currentRow = int(self.findNextRow(col))
        self.cells[currentRow][col] = player
        if self.checkWinner(player,currentRow,col):
            return True
        else:
            return False

    def findNextRow(self, col):
        for r in range(0, self.MAX_ROWS, 1):
            if self.cells[r+1][col] != 0:
                nextClearRow = r
                break
            if self.cells[-1][col] == 0:
                nextClearRow = self.MAX_ROWS
        return nextClearRow

    def isValid(self,col):
        if self.cells[0][col] == 0:
            return 1
        elif not any(0 in x for x in self.cells):
            return 2
        else:
            return 3

    def checkWinner(self, player, row, col):
        #HORIZONTAL columns 0-4 not including 4
        for c in range(0,self.MAX_COLS - 2,1):
            if self.cells[row][c] == player and self.cells[row][c+1] == player and self.cells[row][c+2] == player and self.cells[row][c+3] == player:
                return True
                break
        #VERTICAL WIN
        for r in range(self.MAX_ROWS, 2,-1):
            if self.cells[r][col] == player and self.cells[r-1][col] == player and self.cells[r-2][col] == player and self.cells[r-3][col] == player:
                return True
                break
        #BRUTE FORCE POSITIVE DIAGONAL
        for r in range(3,6,1):
            for c in range(0,4,1):
                if self.cells[r][c] == player and self.cells[r-1][c+1] == player and self.cells[r-2][c+2] == player and self.cells[r-3][c+3] == player:
                    return True
                    break
        #BRUTE FORCE NEGATIVE DIAGONAL
        for r in range(2,-1,-1):
            for c in range(0,4,1):
                if self.cells[r][c] == player and self.cells[r+1][c+1] == player and self.cells[r+2][c+2] == player and self.cells[r+3][c+3] == player:
                    return True
                    break
        return False

users = [1,2]

def main():
    playing = True
    while playing:
        for x, element in enumerate(users):
            turnPlayed = False

            while not turnPlayed:
                board.showGrid()
                try:
                    inp = input("\n" + str(element) + ") Type a Column ")
                    col = int(inp ) - 1
                    if board.isValid(col) == 1:
                        if board.addChip(int(element), col):
                            print ("Winner!")
                        turnPlayed = True
                    elif board.isValid(col) ==2:
                        print("Tie Game!")
                        break
                    elif board.isValid(col) == 3:
                        print("That column is already full! Pick another column.\n")
                except :
                    print("Error! Enter a column number 1-7")

board = Grid()
main()
