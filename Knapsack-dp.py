import timeit
import random
def knapsack(capacity, weights, profit):

    # Check the validation of the inputs
    if (capacity < 0 or len(weights) == 0
        or len(profit) == 0 or len(weights) != len(profit)
            or any( weight < 0 for weight in weights)):
        raise Exception("Invalid input!")

    numItems = len(weights)

    # Create a 2D list that represents our table, each element will be assigned to Zero
    table = [[0 for _ in range(capacity + 1)] for _ in range(numItems + 1)]

    # The Outer loop is for the Rows and the Inner for Columns
    for i in range(1, numItems + 1):
        for cap in range(1, capacity + 1):
            
            if weights[i - 1] <= cap:  # Check if there is a space for the object
                # Consider either including the (current item + any item that can fit) or keep the one from the previous line
                table[i][cap] = max(table[i - 1][cap],
                                   profit[i - 1] + table[i - 1][cap - weights[i - 1]])
            else:
                # If the current item's weight exceeds the capacity, skip it
                table[i][cap] = table[i - 1][cap]

    i = numItems; j = capacity
    selected_items = []
    while(i > 0):
        if table[i][j] == table[i - 1][j]:
            i = i - 1
        else:
            selected_items.append(profit[i - 1]); i = i - 1
            j = j - weights[i]
            

    maxValue = table[numItems][capacity]

    return maxValue, selected_items

n = 30
if (n  < 50): capacity = 100
else: capacity = n * 2
values = [random.randint(10, n * 2) for _ in range(n)]
weights = [random.randint(1, (capacity / 2)) for _ in range(n)]



# Define a lambda function to call your knapsack function
code_to_measure = lambda: knapsack(capacity, weights, values)

# Measure the execution time
execution_time = timeit.timeit(code_to_measure, number=1)

maxValue, selectedItems = knapsack(capacity, weights, values)
print(f"Maximum Value: ", maxValue )
# print(f"Profit of selected items : ", selectedItems ) # prints the Profit value of selected items #*******************************************************
print(f"Execution time: {execution_time} seconds")









