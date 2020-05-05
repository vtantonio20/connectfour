import pygame
import sys
import math

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
        print("\n")

    def clearGrid(self):
        for r in range(len(self.cells)+1):
            for c in range(len(self.cells)):
                self.cells[c][r-1] = 0


    def addChip(self, player, col):
        currentRow = int(self.findNextRow(col))
        self.cells[currentRow][col] = player
        self.addChipGui(player, currentRow, col)
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
            return True
        elif not any(0 in x for x in self.cells):
            return False


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

    def drawBoardGui(self):
        for c in range(self.MAX_COLS +1):
            for r in range(self.MAX_ROWS +2):
                                                #TOPLEFTx        #TOPLEFTY                  #DIMESIONX   #DIMENSIONY
                pygame.draw.rect(screen, BLUE, (c*SQUARE_SIZE, r*SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE - 1, SQUARE_SIZE -1))
                pygame.draw.circle(screen, BLACK, (int(c*SQUARE_SIZE + SQUARE_SIZE/2),int(r*SQUARE_SIZE+ SQUARE_SIZE/2)), RADIUS)

    def addChipGui(self, player, row, col):
        if player == users[1]:
            pygame.draw.circle(screen, RED, (int((SQUARE_SIZE*col + SQUARE_SIZE/2)),(int(SQUARE_SIZE*row + SQUARE_SIZE/2 + SQUARE_SIZE))), RADIUS - 2)
        elif player == users[0]:
            pygame.draw.circle(screen, YELLOW, (int((SQUARE_SIZE*col + SQUARE_SIZE/2 )),(int(SQUARE_SIZE*row + SQUARE_SIZE/2 + SQUARE_SIZE))), RADIUS - 2)


users = [1,2]
BLUE = (0,102,255)
RED = (255,55,0)
YELLOW = (255,255,50)
BLACK = (0,0,0)
WHITE = (255,255,255)

board = Grid()
pygame.init()
pygame.display.set_caption("Connect Four")

SQUARE_SIZE = 100
width = (board.MAX_COLS+1)* SQUARE_SIZE
height = (board.MAX_ROWS + 2) * SQUARE_SIZE
size = (width, height)
RADIUS = int(SQUARE_SIZE/2 - 5)

myFont = pygame.font.SysFont(None, 50)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()


def messageToScreen(msg, color):
    screenText = myFont.render(msg, 1, color)
    screen.blit(screenText, (int(1.5*SQUARE_SIZE),int(SQUARE_SIZE/2)))
def restartGame(restart):
    if restart:
        main()
    else:
        sys.exit()


def main():
    board.clearGrid()
    pygame.draw.rect(screen, BLACK,(0,0, width, SQUARE_SIZE))

    board.drawBoardGui()
    pygame.display.update()

    playing = True
    user = 1
    posx = 0
    won = False

    while playing:
        pygame.display.update()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                restartGame(False)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r and won:
                restartGame(True)

            if event.type == pygame.MOUSEMOTION and not won:
                posx = event.pos[0]
                pygame.draw.rect(screen, BLACK,(0,0, width, SQUARE_SIZE))

            if user == users[0] and not won:
                pygame.draw.circle(screen, RED, (int(posx),(int(SQUARE_SIZE/2))),RADIUS - 5)
            elif user == users[1] and not won:
                pygame.draw.circle(screen, YELLOW, (int(posx),(int(SQUARE_SIZE/2))), RADIUS - 5)


            if event.type == pygame.MOUSEBUTTONDOWN and not won:
                col = math.floor(event.pos[0]/100)
                if board.isValid(col) == 1:
                    if user == 1:
                        user =2
                    else:
                        user = 1
                    if board.addChip(user, col):
                        won = True
                        pygame.draw.rect(screen, BLACK,(0,0, width, SQUARE_SIZE))
                        messageToScreen("Winner! Press r to replay.", WHITE)

                    board.showGrid()
                    pygame.display.update()
                elif board.isValid(col) == False:
                    pygame.draw.rect(screen, BLACK,(0,0, width, SQUARE_SIZE))
                    messageToScreen("Tie Game! Press r to replay.", WHITE)
                    won = True




main()
