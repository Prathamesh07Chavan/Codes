# Fibonacci - Recursive and Non-Recursive

iteration_counter = 0
recursion_counter = 0


# Non-Recursive / Iterative
def fibonacci_iteration(n):
    global iteration_counter
    iteration_counter = 0

    fib_series = []
    previous = 0
    current = 1

    for i in range(n):
        fib_series.append(previous)
        previous, current = current, previous + current
        iteration_counter += 1

    return fib_series


# Recursive
def fibonacci_recursion(n):
    global recursion_counter
    recursion_counter += 1

    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


# Input
n = int(input("Enter number of terms: "))


# Iterative Fibonacci
fib_series = fibonacci_iteration(n)# Get Fibonacci series

print("\nFibonacci using Non-Recursive method:")
print(fib_series)

print("Iteration counter:", iteration_counter)
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")


print("=" * 60)


# Recursive Fibonacci
recursion_counter = 0
fib_series = []

for i in range(n):
    fib_series.append(fibonacci_recursion(i))# Add each result to list  

print("Fibonacci using Recursive method:")
print(fib_series)

print("Recursion counter:", recursion_counter)
print("Time Complexity: O(2^n)")
print("Space Complexity: O(n)")
    
'''Q1. What is Fibonacci series?
A: A series where each number is the sum of the previous two numbers.

Q2. What are the first two Fibonacci numbers?
A: 0 and 1.

Q3. What is recursion?
A: A function calling itself is called recursion.

Q4. Which method is faster?
A: Iterative method.

Q5. Why is recursive Fibonacci slow?
A: Because it calculates the same Fibonacci values repeatedly.

NON-Recursive/iteration
Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

Recursive
Complexity
- Time Complexity: O(2^n) approximately
- Space Complexity: O(n)

Recursive method solves the problem by calling the same function repeatedly, 
while non-recursive method solves it using loops without function calls."
Advantages
1. Simple to understand — demonstrates recursion and iteration clearly.
2. Shows complexity difference — compares O(n) iterative with O(2ⁿ) recursive.
3. Demonstrates recursion — useful for understanding function calls and stack.
4. Easy to implement — requires very little code.
Disadvantages
1. Recursive method is slow for large n because it repeats calculations.
2. Recursive method uses more memory due to function call stack.
3. Basic Fibonacci has limited real-world use compared with more efficient algorithms.

Uses of Fibonacci
1. Algorithm analysis – Used to compare recursive and iterative approaches.
2. Dynamic Programming – Fibonacci is a simple example for learning DP and memoization.
3. Computer algorithms – Used in Fibonacci heaps and some searching techniques.
4. Nature and mathematics – Fibonacci patterns appear in flower arrangements, leaves, and spirals.
5. Financial analysis – Fibonacci ratios are sometimes used in technical analysis of markets.
'''
