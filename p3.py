# Define a class for items to store their weight, profit, and value (profit/weight)
class Item:
    def _init_(self, profit, weight):
        self.profit = profit
        self.weight = weight
        self.value = profit / weight  # Value = profit-to-weight ratio

# Function to solve the fractional knapsack problem
def fractional_knapsack(items, capacity):
    # Sort items by their value in descending order
    items.sort(key=lambda x: x.value, reverse=True)
    
    total_profit = 0  # To store the total profit
    for item in items:
        if capacity >= item.weight:
            # If the knapsack can carry the entire item, take it
            total_profit += item.profit
            capacity -= item.weight
        else:
            # If the knapsack can only carry part of the item, take the fraction
            total_profit += item.value * capacity
            break  # Knapsack is full, so stop
        
    return total_profit

# User Input
if _name_ == "_main_":
    n = int(input("Enter the number of items: "))
    items = []

    for i in range(n):
        profit = float(input(f"Enter profit for item {i+1}: "))
        weight = float(input(f"Enter weight for item {i+1}: "))
        items.append(Item(profit, weight))

    capacity = float(input("Enter the capacity of the knapsack: "))

    # Get the maximum profit
    max_profit = fractional_knapsack(items, capacity)
    print(f"Maximum Profit: {max_profit:.2f}")
