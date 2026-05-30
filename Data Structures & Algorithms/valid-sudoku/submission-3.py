class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row
        # check each column
        # then check every 3X3 Column

        row = len(board)
        col = len(board[0])

        for i in range(row): # checking every row by looping
            currRow = [i for i in board[i] if i.isdigit()] #striping the non numbers
            if len(set(currRow)) != len(currRow): # checking if duplicates with sets
                return False 
        for c in range(col): # checking for col
            currCol = set() # making set to track columns
            for r in range(row):
                if board[r][c].isdigit(): # checking if the thing is a number or a *
                    if board[r][c] in currCol: # if it is in the set 
                        return False # return false
                    else: # if it isnt in here add to the set
                        currCol.add(board[r][c])
        
        # now for the 3X3


        for Br in range(0,9,3): 
            for Bc in range(0,9,3):
                box = set()
                for i in range(3):
                    for j in range(3):
                        if board[Br + i][Bc + j].isdigit():
                            if board[Br + i][Bc + j] in box:
                                return False
                            else:
                                box.add(board[Br + i][Bc + j])
        return True
            