# 0/1 Knapsack using Dynamic Programming

# Take number of items
n = int(input("Enter number of items: "))

profits = []
weights = []

# Take profit and weight of each item
for i in range(n):
    profit = int(input(f"Enter profit of item {i + 1}: "))
    weight = int(input(f"Enter weight of item {i + 1}: "))

    profits.append(profit)
    weights.append(weight)


# Take capacity of knapsack
capacity = int(input("Enter capacity of knapsack: "))


# Create DP table
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)] #row=items (0ton) capacity (0tocpacity) initially 0


# Fill the DP table
for i in range(1, n + 1):

    for w in range(1, capacity + 1):

        # If item can fit
        if weights[i - 1] <= w:

            # Choose maximum of including or excluding item
            dp[i][w] = max(
                profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )

        # If item cannot fit
        else:
            dp[i][w] = dp[i - 1][w]


# Display maximum profit
print("Maximum Profit:", dp[n][capacity])

'''
0/1 Knapsack?  
A problem where each item is either completely selected or not selected.

technique is used here?  
Dynamic Programming.

Time complexity?  
O(n × W), where n is number of items and W is capacity.

Space complexity?  
O(n × W).

. Why not use greedy method?  
Greedy does not always give the optimal solution for 0/1 Knapsack.

Advantages:  
Avoids repeated calculations, gives optimal solutions, and improves efficiency.

Disadvantages:  
Requires extra memory, can be complex to design, and may need large tables.

Dynamic Programming vs Branch & Bound
Dynamic Programming (DP) is generally better when:
- The problem has overlapping subproblems
- There are relatively few possible states
- We can store and reuse previous results
- Example: 0/1 Knapsack, Fibonacci, LCS, Matrix Chain Multiplication

Branch & Bound is generally better when:
- The solution space is huge
- We can calculate a good bound to eliminate many possibilities
- We want to explore only promising solutions
- Example: Travelling Salesman Problem, 0/1 Knapsack, Assignment Problem
'''
