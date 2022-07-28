class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        for i in range(len(board)):
            for j in range(len(board)):
                val = board[i][j]
                if val == '.':
                    continue
                if val in rows[i]:
                    print('a')
                    return False
                rows[i].add(val)
                if val in cols[j]:
                    print('b')
                    return False
                cols[j].add(val)
                idx = (i//3) * 3 + j // 3
                if val in boxes[idx]:
                    print('c')
                    return False
                boxes[idx].add(val)
        return True
            