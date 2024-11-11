# implement 0/1 knapsack problem using dynamic programming.
# time complexity: O(no of items * capacity)
# space complexity: O(no. of items * capacity)

def solve_knapsack_problem(weights, profits, capacity):
    n = len(weights)
    rows = n + 1
    columns = capacity + 1
    
    dp = [[0] * columns for _ in range(rows)] 
    
    for i in range(1, rows):
        for j in range(columns):
            if (weights[i-1] <= j):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]]+profits[i-1])
            else:
                dp[i][j] = dp[i-1][j]

    print('DP table: ')
    for i in range(rows):
        for j in range(columns):
            print(dp[i][j], end=" ")
        print()
    
    return dp[rows - 1][columns - 1]


def main():
    weights = [2, 3, 4, 5]
    profits = [1, 2, 5, 6]
    capacity = 8
    max_profit = solve_knapsack_problem(weights, profits, capacity)
    print(f'Max Profit: {max_profit}')


if __name__ == '__main__':
    main()
