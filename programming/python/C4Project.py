import os, sys, math
import numpy as np
from matplotlib import pyplot as plt, colors
import random

# dict of players
players = {
    "red": 1.0,
    "blue": 2.0
}

# defines number of rows and number of columns
rows, columns = 6, 7

class miniMax:

    def boardScore(self, board, turn):
        '''creates arrays of each row and column and awards it a score
            args:
                board (mxn matrix): only accepts values 0 to 4
                turn (the current player in the form of a string): used to pass into partialBoard check
            returns:
                score: a total score assigned to the whole board
        '''
        score = 0

        arrayMid = [int(i) for i in list((board[columns//2][:]))]
        midCount = arrayMid.count(players[turn])
        score += 10 + midCount * 6

        for x in range(rows):
            arrayRow = [int(i) for i in list(board[x][:])]
            # print(arrayRow, end='    ')
            for y in range(columns-3):
                partialBoard = arrayRow[y:y+4]
                score += self.partialBoardCheck(partialBoard, turn)

        for y in range(columns):
            arrayCol = [int(i) for i in list(board[:][y])]
            # print(arrayCol, end='   ')
            for x in range(rows-3):
                partialBoard = arrayCol[x:x+4]
                score += self.partialBoardCheck(partialBoard, turn)
                # print(arrayCol)
        # print(score)
        for x in range(rows-3):
            for y in range(columns-3):
                partialBoard = [board[x+i-1][y+i-1] for i in range(4)]
                score += self.partialBoardCheck(partialBoard, turn)

        for x in range(rows-3):
            for y in range(columns-3):
                partialBoard = [board[x+3-i-1][y+i-1] for i in range(4)]
                score += self.partialBoardCheck(partialBoard, turn)

        return score

    def partialBoardCheck(self, partialBoard, turn):
        '''checks each array created by self.boardScore() and awards it a score

            args:
                partialBoard (list created by self.boardScore()): used to generate score
                turn: used to count specific numbers in the arrays

            Returns:
                Score for the partialBoard
        '''
        score = 0
        if partialBoard.count(players['blue']) == 4:
            score += 500
        elif partialBoard.count(players['blue']) == 3 and partialBoard.count(0.0) == 1:
            score += 5
        elif partialBoard.count(players['blue']) == 2 and partialBoard.count(0.0) == 2:
            score =+ 2
        

        if partialBoard.count(players['red']) == 4:
            score -= 50
        elif partialBoard.count(players['red']) == 3 and partialBoard.count(0.0) == 1:
            score -= 5
        


        return score

    def validLocation(self, board):
        '''returns all valid column values that are considered legal moves

            args:
                board (mxn matrix): only accepts values 0 to 4
            
            Returns:
                validLocations (list): list of all legal moves in the form of their column value
        '''
        validLocations = []
        for col in range(columns):
            dumb = board[col]
            if dumb[0] == 0:
                validLocations.append(col)
        return validLocations

    def bestMove(self, board, player):
        '''Takes in scores from all columns and returns the column that gives the highest score
            (depreciated since implementation of miniMax algorithm)

            args:
                board (mxn matrix): only accepts values 0 to 4
                player(str): value of player ('red' or 'blue')
            
            Returns:
                bestColumn (int): the column that yielded the highest score
        '''
        validLocations = self.validLocation(board)
        bestScore = 0
        # print(validLocations)
        bestColumn = random.choice(validLocations)
        for col in validLocations:
            tmpBoard = board.copy()
            count = tmpBoard[col]
            rowOfCol = -1
            while count[rowOfCol] != 0:
                rowOfCol -= 1
                # self.printBoard()
            count[rowOfCol] = players[player]
            score = self.boardScore(tmpBoard, turn)
            if score > bestScore:
                bestScore = score
                bestColumn = col
        # print(bestColumn + 1)
        return bestColumn

    def findTerminalNode(self, board):
        '''determine if node is terminal or not

            args:
                board (mxn matrix): only accepts values 0 to 4

            returns:
                bool
        '''
        return game.findWinner(board, 'red') or game.findWinner(board, 'blue') or len(self.validLocation(board)) == 0

    def miniMaxAlgo(self, board, depth, alpha, beta, maximizingPlayer):
        '''the minimax algorithm creates a series of nodes of possible moves, 
        generating a score for each outcome depth number of moves in the future.

            args:
                board (mxn matrix): only accepts values 0 to 4
                depth (int): number or nodes created into the future
                alpha (int): used to stop unneccessary nodes
                beta (int): used to stop unneccessary nodes
                maximizingPlayer (bool): whether the currect player is maximising or not
            
            Returns:
                tuple (
                    bescolumn (int): the column with the highest score from the future
                    value (int): the value of the score from the future (debugging purposes only)
                )
        '''
        validLocations = self.validLocation(board)
        # print(validLocations)
        terminal = self.findTerminalNode(board)
        if depth == 0 or terminal:
            if terminal:
                if game.findWinner(board, 'blue'):
                    return (None, 99999999)
                elif game.findWinner(board, 'red'):
                    return (None, -9999999)
                else:
                    return (None, 0)
            else:
                return (None, self.boardScore(board, 'blue'))
        if maximizingPlayer:
            value = -math.inf
            bescolumn = random.choice(validLocations)
            for col in validLocations:
                tmpBoard = board.copy()
                count = tmpBoard[col]
                rowOfCol = -1
                while count[rowOfCol] != 0:
                    rowOfCol -= 1
                    # self.printBoard()
                count[rowOfCol] = players['blue']
                newScore = self.miniMaxAlgo(tmpBoard, depth-1, alpha, beta, False)[1]
                if newScore > value:
                    value = newScore
                    bescolumn = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            # print(bescolumn, value)
            return bescolumn, value
        else:
            value = math.inf
            bescolumn = random.choice(validLocations)
            for col in validLocations:
                tmpBoard = board.copy()
                count = tmpBoard[col]
                rowOfCol = -1
                while count[rowOfCol] != 0:
                    rowOfCol -= 1
                    # self.printBoard()
                count[rowOfCol] = players['red']
                newScore = self.miniMaxAlgo(tmpBoard, depth-1, alpha, beta, True)[1]
                if newScore < value:
                    value = newScore
                    bescolumn = col
                    beta = min(beta, value)
                    if alpha >= beta:
                        break
            # print(bescolumn, value)
            return bescolumn, value
            
        
            

# contains functions to run connect
class game:

    def matPlot(self, currentBoard):
        '''Plots a graph of the currentBoard using matplotlib

            args:
                currectBoard (mxn matrix): only accepts values 0 to 4
        '''
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
        '''Loops through the board and finds groups of 4

            args:
                board (mxn matrix): only accepts values 0 to 4
                player (str): used to referance similar items in matrix
            returns:
                bool
        '''
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
                self.selectedColumn = int(input('{}\'s turn (1-{}): '.format(turn.capitalize(), columns))) - 1
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
        # self.matPlot(np.fliplr(np.rot90(board, k = 3)))

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
        rowOfCol = -1
        while col[rowOfCol] != 0:
            rowOfCol -= 1
            # self.printBoard()
        col[rowOfCol] = players[player]
        if self.findWinner(board, turn) is True:
            # print('\033c')
            self.printBoard()
            self.matPlot(np.fliplr(np.rot90(board, k = 3)))
            print('{} won! Congratulations!'.format(turn.capitalize()))
            
            restart = input('Play Again? Y/n: ').lower() or 1
            if restart == 'y' or restart == 1:
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                sys.exit()
        return



if __name__ == "__main__":
    # initiates class and containes main game loop
    game = game()
    mm = miniMax()
    board = game.initiateBoard()
    turn = 'red'
    minimaxonoff = input('Would you like to play against the AI? Y/n: ').lower() or 1
    while True:
        # print('\033c')
        game.printBoard()
        game.matPlot(np.fliplr(np.rot90(board, k = 3)))
        game.flag = False
        if turn == 'red':
            game.checkPlayer(int(game.selectColumn()), turn)
        else:
            if minimaxonoff == 'y' or minimaxonoff == 1:
                game.insertPlayer(mm.miniMaxAlgo(board, 6, -math.inf, math.inf, True)[0], turn)
            else:
                game.checkPlayer(int(game.selectColumn()), turn)
            
        turn = 'blue' if turn == 'red' else 'red'
