def knapsack(capacity, weights, values):
    n = len(weights)

    # Initialize a 2D table to store the maximum value for each capacity and item count.
    dp = [[0] * (capacity+1)]*(n+1)

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the current item's weight exceeds the current capacity, skip it.
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # Otherwise, consider either including the item or excluding it.
                dp[i][w] = max(dp[i - 1][w], dp[i - 1]
                               [w - weights[i - 1]] + values[i - 1])

    # Trace back to find the items selected.
    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    # Reverse the list of selected items to maintain the original order.
    selected_items.reverse()

    # Return the maximum value and the list of selected items.
    return dp[n][capacity], selected_items


if __name__ == "__main__":
    capacity = 30
    values = [21 , 12 , 22 , 10 , 23 , 27 , 4 , 19 , 20 , 2 , 25 , 23 , 29 , 23 , 21 , 21 , 14 , 2 , 2 , 29 , 12 , 15 , 22 , 18 , 8 , 9 , 14 , 19 , 12 , 24 , 11 , 26 , 2 , 9 , 2 , 27 , 17 , 23 , 3 , 2 , 22 , 26 , 9 , 17 , 9 , 2 , 12 , 20 , 8 , 20 , 11 , 27 , 6 , 23 , 4 , 2 , 2 , 19 , 28 , 13 , 17 , 4 , 2 , 23 , 14 , 18 , 6 , 1 , 15 , 23 , 7 , 17 , 19 , 8 , 14 , 6 , 11 , 24 , 25 , 15 , 8 , 16 , 4 , 14 , 3 , 8 , 8 , 15 , 13 , 30 , 28 , 4 , 25 , 2 , 24 , 14 , 5 , 24 , 18 , 27 ]
    weights = [19 , 21 , 23 , 23 , 30 , 2 , 3 , 25 , 16 , 16 , 6 , 13 , 19 , 1 , 17 , 17 , 25 , 2 , 28 , 22 , 24 , 12 , 16 , 16 , 2 , 23 , 24 , 14 , 3 , 11 , 11 , 7 , 1 , 12 , 11 , 9 , 25 , 12 , 27 , 16 , 16 , 29 , 29 , 17 , 10 , 5 , 28 , 11 , 26 , 18 , 10 , 4 , 12 , 30 , 16 , 26 , 4 , 26 , 5 , 1 , 2 , 10 , 19 , 17 , 26 , 8 , 22 , 21 , 10 , 7 , 17 , 21 , 8 , 25 , 21 , 29 , 23 , 9 , 24 , 28 , 15 , 6 , 23 , 16 , 9 , 2 , 29 , 11 , 22 , 17 , 30 , 7 , 8 , 30 , 1 , 14 , 7 , 2 , 22 , 26]
    max_value, selected_items = knapsack(capacity, weights, values)
    print("Maximum Value:", max_value)
    print("Selected Items (0-based index):", selected_items)

    capacity = 30
    values = [2, 2, 4, 5, 3]
    weights = [3, 1, 3, 4, 2]
    max_value, selected_items = knapsack(capacity, weights, values)
    print("Maximum Value:", max_value)
    print("Selected Items (0-based index):", selected_items)
