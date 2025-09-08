def get_array():
    n = int(input("Enter number of elements: "))  # size of array
    arr = []
    max_profit=0
    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        arr.append(num)
    print("Array is:", arr)
    
    for i in range(0, n-1):
        if arr[i+1]>arr[i]:
            max_profit=arr[i+1]-arr[i]
    print("Maximum profit is:", max_profit)
get_array()

# Problem: Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:   
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
# Constraints:
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
# Approach:
# 1. Iterate through the array and check for every pair of consecutive days if selling on the next day yields a profit.
# 2. If it does, calculate the profit and update the maximum profit if this profit is higher than the previously recorded maximum profit.
# Time Complexity: O(n)
