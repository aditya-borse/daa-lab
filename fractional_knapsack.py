# solve factional knapsack problem using greedy strategy
# time complexity: O(n*log(n))
# space complexity: O(n)

class Item:
    def __init__(self, weight, profit, number):
        self.weight = weight
        self.profit = profit
        self.number = number
        self.ratio = profit/weight


def build_sack(weights, profits):
    sack = []
    i = 1
    for weight, profit in zip(weights, profits):
        item = Item(weight, profit, i)
        sack.append(item)
        i += 1
    return sack


def solve_fractional_knapsack(sack, capacity):
    for item in sack:
        item.ratio = item.profit / item.weight

    sack.sort(key=lambda item:item.ratio, reverse=True)
    total_profit = 0
    included_items = []

    for item in sack:
        if item.weight <= capacity:
            capacity = capacity - item.weight
            total_profit = total_profit + item.profit
            included_items.append(item.number)
        else:
            total_profit = total_profit + ((capacity/item.weight)*item.profit)
            included_items.append(item.number)
            break
    
    return total_profit, included_items


def main():
    weights = [2, 3, 5, 7, 1, 4, 1]
    profits = [10, 5, 15, 7, 6, 18, 3]
    capacity = 15
    sack = build_sack(weights, profits)
    total_profit, included_items = solve_fractional_knapsack(sack, capacity)
    print(f'Total profit: {total_profit}')
    print(f'Included items: {included_items}')


if __name__ == '__main__':
    main()