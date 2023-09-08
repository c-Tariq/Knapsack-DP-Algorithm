import numpy as np

def knapsack(capacity, weights, values):
    n = len(weights)
    
    # Create a 2D NumPy array to store the maximum values for subproblems
    dp = np.zeros((n + 1, capacity + 1), dtype=int)

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Consider either including the current item or excluding it
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else : 
                # If the current item's weight exceeds the capacity, skip it
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][capacity]
    
    return max_value





if __name__ == "__main__":
    # capacity = 10
    # values = [1, 4, 8, 5]
    # weights = [3, 3, 5, 6]
    # max_value = knapsack(capacity, weights, values)
    # print("Maximum Value:", max_value)

    capacity = 7
    values = [2, 2, 4, 5, 3]
    weights = [3, 1, 3, 4, 2]
    max_value = knapsack(capacity, weights, values)
    print("Maximum Value:", max_value)