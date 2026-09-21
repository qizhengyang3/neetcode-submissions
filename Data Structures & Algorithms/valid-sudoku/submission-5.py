class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(list)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for x in range(9):
            for y in range(9):
                if board[x][y] == '.':
                    continue
                if (board[x][y] in cols[y]
                    or board[x][y] in rows[x] 
                    or board[x][y] in squares[x//3, y//3]):
                    return False
                cols[y].append(board[x][y])
                rows[x].add(board[x][y])
                squares[x//3, y//3].add(board[x][y])

        return True