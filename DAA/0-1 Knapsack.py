# Practical 4
# Write a program to solve a 0-1 Knapsack problem using dynamic programming.

# Dynamic Programming Approach
def knapsack_01(n, values, weights, W):
    # Create a 2D DP table initialized with zeros
    dp = [[0] * (W+1) for _ in range(n+1)]

    # Fill the DP table
    for i in range(n+1):
        for w in range(W+1):
            # Base case: no items or no capacity
            if i == 0 or w == 0:
                dp[i][w] = 0
            # If current item's weight can fit in the knapsack
            elif weights[i-1] <= w:
                # Take maximum of including or excluding current item
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            # If current item's weight exceeds capacity
            else:
                # Exclude current item
                dp[i][w] = dp[i-1][w]
    
    # Backtrack to find selected items
    selected_items = []
    i, w = n, W
    while i > 0 and w > 0:
        # If current item was included
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
        i -= 1
    
    # Return maximum value and list of selected items
    return dp[n][W], selected_items

if __name__ == "__main__":
    # Test case
    n = 3  # Number of items
    values = [60, 100, 120]  # Values of items
    weights = [10, 20, 30]   # Weights of items
    W = 50  # Knapsack capacity

    # Solve the knapsack problem
    max_value, selected_items = knapsack_01(n, values, weights, W)
    print("Maximum value:", max_value)
    print("Selected items:", selected_items)

