def numTrees(n):
    dp = [0] * (n+1) #array of size n+1
    #base case
    dp[0] = dp[1] = 1
    
    #bottom-up dynamics
    for i in range(2, n+1):
        for j in range(1, i+1):
            dp[i] += dp[j-1] * dp[i-j]
    
    return dp[n]

'''Bottom-up dynamic programming is used to solve LeetCode Question 96 - Unique Binary Search Trees. The goal is to find the number of structurally unique binary search trees that store values from `1` to `n`.

Let's see how bottom-up dynamic programming is applied to solve this problem:

1. Identify the subproblems:
   The subproblem here is finding the number of unique binary search trees for a given `n`, where `n` can range from `1` to the target value.

2. Define the base case:
   For `n = 0`, there is exactly one unique binary search tree, an empty tree (represented as `None`).
   For `n = 1`, there is also exactly one unique binary search tree, a tree with a single node.

3. Initialize the data structure:
   We create an array `dp` of size `n + 1` to store the number of unique BSTs for each value of `n`. We initialize `dp[0]` and `dp[1]` to `1` as they represent the base cases.

4. Build up the solutions:
   We use a loop to iteratively calculate the number of unique BSTs for each value of `n` from `2` to `n`. For each `n`, we consider each number from `1` to `n` as the root of the BST. The number of unique BSTs with a specific number as the root can be calculated using the number of unique BSTs in its left subtree (values from `1` to `j - 1`) and the number of unique BSTs in its right subtree (values from `j + 1` to `n`). The total number of unique BSTs for `n` is the sum of the unique BSTs with each number as the root.

5. Return the final solution:
   After the loop completes, `dp[n]` will contain the number of structurally unique binary search trees that store values from `1` to `n`. We return `dp[n]` as the final solution.
'''
