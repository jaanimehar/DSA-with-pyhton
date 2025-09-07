class Solution:
    def nextPermutation(self, arr):
        n=len(arr)
        i=n-2
        while i>=0 and arr[i]>=arr[i+1]:
            i-=1
        if i>=0:
            j=n-1
            while arr[j]<=arr[i]:
                j-=1
            arr[i],arr[j]=arr[j],arr[i]
        arr[i+1:]=reversed(arr[i+1:])
        return arr  
# Example usage:
solution = Solution()
print(solution.nextPermutation([1,3,4,5]))  # Output: [1, 3, 2]
# This function modifies the input list to the next permutation in place and returns it.
# Problem: Next Permutation
# Given an array of integers nums, find the next permutation of nums.
# The replacement must be in place and use only constant extra memory.
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]
# Example 4:
# Input: nums = [1]
# Output: [1]
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
# Approach:
# 1. Traverse the array from the end to find the first decreasing element (pivot).
# 2. If found, traverse again from the end to find the first element greater than the pivot and swap them.
# 3. Reverse the elements after the pivot index to get the next permutation.    # 4. If no pivot is found, reverse the entire array to get the lowest permutation.  # Time Complexity: O(n)
# Space Complexity: O(1)# 4. If no pivot is found, reverse the entire array to get the lowest permutation.  # Time Complexity: O(n)
# Space Complexity: O(1)    # 4. If no pivot is found, reverse the entire array to get the lowest permutation.  # Time Complexity: O(n)
# Space Complexity: O(1)
        