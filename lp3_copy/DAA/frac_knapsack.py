# Fractional Knapsack using Greedy Method

# Take number of items
n = int(input("Enter number of items: "))

items = []

# Take profit and weight of each item
for i in range(n):
    profit = int(input(f"Enter profit of item {i + 1}: "))
    weight = int(input(f"Enter weight of item {i + 1}: "))

    # Calculate profit/weight ratio
    ratio = profit / weight

    # Store item details
    items.append((profit, weight, ratio))


# Take capacity of knapsack
capacity = int(input("Enter capacity of knapsack: "))


# Sort items by profit/weight ratio in descending order
items.sort(key=lambda x: x[2], reverse=True)


total_profit = 0

# Select items
for profit, weight, ratio in items:

    # If complete item can fit
    if capacity >= weight:
        capacity -= weight
        total_profit += profit

    # If only part of item can fit
    else:
        total_profit += ratio * capacity
        capacity = 0
        break


# Display maximum profit
print("Maximum Profit:", total_profit)

'''
Fractional Knapsack?  
It is a problem where we can take whole or fractional parts of items to maximize profit within a given capacity
Time complexity O(n log n) because we sort the items.
Space complexity O(n) for storing the items.
✅ Advantages
1. Simple and easy to implement.
2. Greedy method gives the optimal solution for Fractional Knapsack.
3. Fast because it mainly requires sorting.
4. Items can be divided into fractions.
❌ Disadvantages
1. It works only when items can be divided.
2. Greedy method does not always work for 0/1 Knapsack.
3. Sorting is required before selecting items.
🔹 Uses
1. Cargo loading — selecting goods to maximize value within limited space.
2. Resource allocation — distributing limited resources for maximum benefit.
3. Investment/budget allocation — selecting portions of investments within a limited budget.
4. Transport and logistics — maximizing value when goods can be partially loaded.
'''
