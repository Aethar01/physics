# %%
import os, sys
import numpy as np
from matplotlib import pyplot as plt, image, colors

# dict of players
players = {
    "red": 1,
    "blue": 2
}

# defines number of rows and number of columns
rows, columns = 6, 7

# contains functions to run connect
class game:

    def matPlot(self, currentBoard):
        plt.imshow(currentBoard)
        cmap = colors.ListedColormap(['#202020', '#ac4141', '#6c99ba', '#7d0a0a', '#093e63'])
        plt.style.use("dark_background")
        bounds=[0,1,2,3,4,5]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        img = plt.imshow(currentBoard, interpolation='nearest', cmap=cmap, norm=norm, extent=[1,columns+1,1,rows+1])
        plt.colorbar(img, boundaries=bounds, ticks=[0, 1, 2, 3])
        plt.grid()
        plt.show()

    def findWinner(self, board, player):
        '''Loops through the board and finds groups of 4'''
        # Check horizontal locations for win
        # global board
        for y in range(rows-3):
            for x in range(columns):
                if board[x][y] == players[player] and board[x][y+1] == players[player] and board[x][y+2] == players[player] and board[x][y+3] == players[player]:
                    board[x][y] = players[player] + 2
                    board[x][y+1] = players[player] + 2
                    board[x][y+2] = players[player] + 2
                    board[x][y+3] = players[player] + 2
                    return True
    
        # Check vertical locations for win
        for y in range(rows):
            for x in range(columns-3):
                if board[x][y] == players[player] and board[x+1][y] == players[player] and board[x+2][y] == players[player] and board[x+3][y] == players[player]:
                    board[x][y] = players[player] + 2
                    board[x+1][y] = players[player] + 2
                    board[x+2][y] = players[player] + 2
                    board[x+3][y] = players[player] + 2
                    return True
    
        # Check positively sloped diaganols
        for y in range(rows-3):
            for x in range(columns-3):
                if board[x][y] == players[player] and board[x+1][y+1] == players[player] and board[x+2][y+2] == players[player] and board[x+3][y+3] == players[player]:
                    board[x][y] = players[player] + 2
                    board[x+1][y+1] = players[player] + 2
                    board[x+2][y+2] = players[player] + 2
                    board[x+3][y+3] = players[player] + 2
                    return True
    
        # Check negatively sloped diaganols
        for y in range(rows-3):
            for x in range(3, columns):
                if board[x][y] == players[player] and board[x-1][y+1] == players[player] and board[x-2][y+2] == players[player] and board[x-3][y+3] == players[player]:
                    board[x][y] = players[player] + 2
                    board[x-1][y+1] = players[player] + 2
                    board[x-2][y+2] = players[player] + 2
                    board[x-3][y+3] = players[player] + 2
                    return True

    def __init__(self):
        '''flag to prevent recurrsion'''
        self.flag = False

    def selectColumn(self):
        '''calls user input to select a column w/ missinput checking'''
        while True:
            try:
                self.selectedColumn = int(input('{}\'s turn (1-7): '.format(turn))) - 1
                if self.selectedColumn not in range(0, columns):
                    raise IndexError
                return self.selectedColumn
            except ValueError:
                print('That\'s not a number!')
                continue
            except IndexError:
                print('That number is not a column!')
                continue
            break

    def initiateBoard(self):
        '''creates the matrix used to contain player moves'''
        self.board = np.zeros((columns, rows))
        return self.board

    def printBoard(self):
        '''prints the board and reformats to be the correct way up'''
        print(' ', end='')
        for i in range(1, columns):
            print('', "{:02d}".format(i), end='')
        print('', "{:02d}".format(columns))
        # print('  '.join(map(str, range(columns))))
        # print('  1  2  3  4  5  6  7')
        print(np.fliplr(np.rot90(board, k = 3)))
        self.matPlot(np.fliplr(np.rot90(board, k = 3)))

    def checkPlayer(self, column, player):
        '''check if player column choice is viable and call for input again if not'''
        col = self.board[column]
        try:
            if col[0] != 0:
                print('The column is full!')
                raise Exception('The column is full!')
        except:
            self.checkPlayer(int(self.selectColumn()), turn)
        if self.flag is False:
            self.insertPlayer(self.selectedColumn, turn)
            self.flag = True
        
    def insertPlayer(self, column, player):
        '''insert player id into board'''
        col = self.board[column]
        poop = -1
        while col[poop] != 0:
            poop -= 1
            # self.printBoard()
        col[poop] = players[player]
        if self.findWinner(board, turn) is True:
            # print('\033c')
            self.printBoard()
            print('{} won! Congratulations!'.format(turn))
            
            restart = input('Play Again? Y/n: ').lower() or 404
            if restart == 'y' or restart == 404:
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                sys.exit()
        return


if __name__ == "__main__":
    # initiates class and containes main game loop
    game = game()
    board = game.initiateBoard()
    turn = 'red'
    while True:
        # print('\033c')
        game.printBoard()
        # game.matPlot(np.fliplr(np.rot90(board, k = 3)))
        game.flag = False
        game.checkPlayer(int(game.selectColumn()), turn)
        turn = 'blue' if turn == 'red' else 'red'
