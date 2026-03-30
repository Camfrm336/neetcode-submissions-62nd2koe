class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowVisit = defaultdict(set)
        colVisit = defaultdict(set)
        squares = defaultdict(set)
        ROWS, COLS = len(board), len(board[0])

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == ".":
                    continue
                
                if (board[i][j] in rowVisit[i] or board[i][j] in colVisit[j] or board[i][j] in squares[(i //3, j//3)]):
                    return False
                rowVisit[i].add(board[i][j])
                colVisit[j].add(board[i][j])
                squares[(i//3,j//3)].add(board[i][j])
        return True

        