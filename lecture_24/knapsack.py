def knapsack(weights, prices, capacity, index = 0):
    if index == len(weights) or capacity == 0:
        return 0
    left = 0
    if capacity >= weights[index]:
        left = prices[index] + knapsack(weights, prices, capacity - weights[index], index + 1)
    right = knapsack(weights, prices, capacity, index + 1)
    return max(left, right)

p = [7, 8, 6]
w = [10, 15, 5]
print(knapsack(w, p, 20))