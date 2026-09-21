class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_time = [0] * 10

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                num_time[int(board[i][j])] += 1
            for cnt in num_time:
                if cnt > 1:
                    return False
            num_time = [0] * 10

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[j][i] == '.':
                    continue
                num_time[int(board[j][i])] += 1
            for cnt in num_time:
                if cnt > 1:
                    return False
            num_time = [0] * 10

        
        x = 0
 
        for m in range(3):

            for i in range(0 + x, 3 + x):
                for j in range(3):
                    if board[i][j] == '.':
                        continue
                    num_time[int(board[i][j])] += 1
                for cnt in num_time:
                    if cnt > 1:
                        return False
            num_time = [0] * 10
            x += 3

        x = 0
 
        for m in range(3):

            for i in range(0 + x, 3 + x):
                for j in range(3,6):
                    if board[i][j] == '.':
                        continue
                    num_time[int(board[i][j])] += 1
                for cnt in num_time:
                    if cnt > 1:
                        return False
            num_time = [0] * 10
            x += 3

        x = 0
 
        for m in range(3):

            for i in range(0 + x, 3 + x):
                for j in range(6,9):
                    if board[i][j] == '.':
                        continue
                    num_time[int(board[i][j])] += 1
                for cnt in num_time:
                    if cnt > 1:
                        return False
            num_time = [0] * 10
            x += 3

        return True