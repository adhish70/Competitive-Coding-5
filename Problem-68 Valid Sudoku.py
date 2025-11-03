# 36. Valid Sudoku

# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        #Row
        for i in range(n):
            Hashset = set()
            for j in range(n):
                if board[i][j] != ".":
                    if board[i][j] not in Hashset:
                        Hashset.add(board[i][j])
                    else:
                        return False

        #Col
        for i in range(n):
            Hashset = set()
            for j in range(n):
                if board[j][i] != ".":
                    if board[j][i] not in Hashset:
                        Hashset.add(board[j][i])
                    else:
                        return False

        #3x3 blocks
        for x in range(0, n, 3):
            for y in range (0, n, 3):
                Hashset = set()
                for i in range(x, x+3):
                    for j in range(y, y+3):
                        if board[i][j] != ".":
                            if board[i][j] not in Hashset:
                                Hashset.add(board[i][j])
                            else:
                                return False

        return True           