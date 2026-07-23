class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])

        for r in range(row):
            stripedRow = [i for i in board[r] if i.isdigit()]
            if len(set(stripedRow)) != len(stripedRow):
                return False
        for c in range(col):
            currCol = set()
            for r in range(row):
                if board[r][c].isdigit():
                    if board[r][c] in currCol:
                        return False
                    else:
                        currCol.add(board[r][c])
        print('test')
        for boardR in range(0,9,3):
            for boardC in range(0,9,3):
                print(boardR,boardC)
                currbox = set()
                for r in range(3):
                    for c in range(3):
                        if board[boardR + r][boardC + c].isdigit():
                            if board[boardR + r][boardC + c] in currbox:
                                return False
                            else:
                                currbox.add(board[boardR + r][boardC + c])
        return True

                
            

        