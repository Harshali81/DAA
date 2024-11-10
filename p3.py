class Item:
    def __init__(self, id, value, weight):
        self.id = id
        self.value = value
        self.weight = weight

# Function to calculate the maximum value of the knapsack
def fractional_knapsack(capacity, items):
    # Calculate value to weight ratio for each item
    for item in items:
        item.ratio = item.value / item.weight
    
    # Sort items by value to weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0  # Total value of knapsack

    for item in items:
        if capacity <= 0:  # If the knapsack is full
            break
        
        if item.weight <= capacity:
            # If the item can fit in the knapsack
            total_value += item.value
            capacity -= item.weight
        else:
            # Take the fractional part of the item
            total_value += item.value * (capacity / item.weight)
            capacity = 0  # Knapsack is now full

    return total_value

# Input from the user
if __name__ == "__main__":
    capacity = float(input("Enter the capacity of the knapsack: "))
    n_items = int(input("Enter the number of items: "))

    items = []

    # Input item details
    for i in range(n_items):
        item_id = input(f"Enter Item ID for Item {i + 1}: ")
        value = float(input(f"Enter Value for Item {i + 1}: "))
        weight = float(input(f"Enter Weight for Item {i + 1}: "))
        items.append(Item(item_id, value, weight))

    # Calculate maximum value
    max_value = fractional_knapsack(capacity, items)

    # Output the maximum value
    print(f"Maximum value in the knapsack: {max_value:.2f}")

  """
 PS C:\Users\HP> python -u "c:\Users\HP\Downloads\p3.py"
Enter the capacity of the knapsack: 50
Enter the number of items: 3
Enter Item ID for Item 1: A
Enter Value for Item 1: 60
Enter Weight for Item 1: 10
Enter Item ID for Item 2: B
Enter Value for Item 2: 100
Enter Weight for Item 2: 20
Enter Item ID for Item 3: C
Enter Value for Item 3: 120
Enter Weight for Item 3: 30
Maximum value in the knapsack: 240.00
PS C:\Users\HP> 
"""
