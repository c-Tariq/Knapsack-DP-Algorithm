def knapsack(capacity, weights, values):
    n = len(weights)

    # Initialize a 2D table to store the maximum value for each capacity and item count.
    dp = [[0]* (capacity+1) ]*(n+1)

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the current item's weight exceeds the current capacity, skip it.
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # Otherwise, consider either including the item or excluding it.
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

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
    capacity = 10
    values = [1, 4, 8, 5]
    weights = [3, 3, 5, 6]
    max_value, selected_items = knapsack(capacity, weights, values)
    print("Maximum Value:", max_value)
    print("Selected Items (0-based index):", selected_items)

    capacity = 7
    values = [2, 2, 4, 5, 3]
    weights = [3, 1, 3, 4, 2]
    max_value, selected_items = knapsack(capacity, weights, values)
    print("Maximum Value:", max_value)
    print("Selected Items (0-based index):", selected_items)