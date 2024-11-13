# implement the n queens problem using backtracking
# time complexity: O(n!)
# space complexity: O(n^2)

def solveNQueens(n):
    board = [['.'] * n for _ in range(n)]
    col = set()
    posDiag = set()
    negDiag = set()
    res = []

    def backtrack(r):
        if (r == n):
            copy = [''.join(row) for row in board]
            res.append(copy)
            return
        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)

            board[r][c] = 'Q'

            backtrack(r+1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = '.'
    
    backtrack(0)
    return res

def main():
    n = 8
    res = solveNQueens(n)
    for idx, solution in enumerate(res):
        print(f'Solution {idx + 1}:')
        for row in solution: 
            print(row)

if __name__ == '__main__':
    main()
