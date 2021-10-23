from itertools import chain, groupby
nothing = '.'
red = 'R'
blue = 'B'
neededToWin = 4

class game:
    
    def initiateGrid(self, TotColums = 9, TotRows = 6):
        '''Create variables for the C4 grid'''
        self.TotColums = TotColums
        self.TotRows = TotRows
        self.grid = [[nothing] * TotRows for _ in range(TotColums)]
    
    def insertTok(self, column, colour):
        '''Insert colour in column of users choice'''
        col = self.grid[column]
        if col[0] != nothing:
            raise Exception("Column is full up!")
        poop = -1
        while col[poop] != nothing:
            poop -= 1
        col[poop] = colour
        self.checkWinner()

    def checkWinner(self):
        '''Check for a winner on the grid'''
        winner = self.poopOutWinner()
        if winner:
            self.printPoopyGrid()
            raise Exception(winner + ' destroyed the competition!')
    
    def poopOutWinner(self):
        '''Return who the winner is'''
        lines = (
            self.grid,
            zip(*self.grid)
        )

        for line in chain(*lines):
            for colour, group in groupby(line):
                if colour != nothing and len(list(group)) >= neededToWin:
                    return colour
    
    def printPoopyGrid(self):
        '''just prints the grid out, what did you expect lmao'''
        print(' '.join(map(str, range(self.TotColums))))
        for cum in range(self.TotRows):
            print(' '.join(str(self.grid[yep][cum]) for yep in range(self.TotColums)))
        print()
        




if __name__ == '__main__':
    game = game()
    game.initiateGrid()
    turn = red
    while True:
        game.printPoopyGrid()
        row = input('{}\'s turn: '.format('Red' if turn == red else 'Blue'))
        game.insertTok(int(row), turn)
        turn = blue if turn == red else red
    