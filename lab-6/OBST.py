"""
Develop a program to implement Optimal Binary Search Tree using 
Dynamic Programming.
"""


def optimal_bst(keys, freq, n):
    
    cost = [[0 for _ in range(n)] for _ in range(n)]
    root = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]
        root[i][i] = i

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            cost[i][j] = float('inf')
            
            for r in range(i, j + 1):
                c = (cost[i][r-1] if r > i else 0) + \
                    (cost[r+1][j] if r < j else 0) + \
                    sum(freq[i:j+1])
                
                if c < cost[i][j]:
                    cost[i][j] = c
                    root[i][j] = r

    return cost, root

# Example
keys = [10, 20, 30]
freq = [3, 2, 5]
n = len(keys)

cost, root = optimal_bst(keys, freq, n)
print(f"Optimal BST cost: {cost[0][n-1]}")
print(f"Root element: {keys[root[0][n-1] - 1]}")
