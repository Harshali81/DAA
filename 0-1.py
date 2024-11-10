def knapsack(weights, values, capacity):
    n = len(values)  # Number of items

    # Create a DP table to store maximum values for each weight limit
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # Check if the weight of the current item is less than or equal to the current capacity
            if weights[i - 1] <= w:
                # Include the current item and check if this gives a better value
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Exclude the current item
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]  # The bottom-right cell will contain the maximum value


# Input from the user
if __name__ == "__main__":
    capacity = int(input("Enter the capacity of the knapsack: "))
    n_items = int(input("Enter the number of items: "))

    weights = []
    values = []

    # Input item details
    for i in range(n_items):
        value = int(input(f"Enter Value for Item {i + 1}: "))
        weight = int(input(f"Enter Weight for Item {i + 1}: "))
        values.append(value)
        weights.append(weight)

    # Calculate maximum value
    max_value = knapsack(weights, values, capacity)

    # Output the maximum value
    print(f"Maximum value in the knapsack: {max_value}")
