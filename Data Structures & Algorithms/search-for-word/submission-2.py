class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = set()

        def backtrack(r,c,index):
            if  not (0<= r < row and 0<= c < col):
                return False # out of bounds
            if (r,c) in visited or board[r][c] != word[index]: # we have seen this pair
                return False
            if index == len(word) - 1:
                return True
            visited.add((r,c))
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if backtrack(nr,nc,index + 1):
                    visited.remove((r,c))
                    return True
            visited.remove((r,c))
            return False
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if backtrack(r,c,0):
                        return True
        return False
                    
        