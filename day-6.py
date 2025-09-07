class Solution:
    def findMajority(self, arr):
        
        n=len(arr)
        occur=n//3
        result=[]
        
        for i in range(n):
            count=0
            
            for j in range(n):
                
                if arr[i]==arr[j]:
                    count+=1
            
            if count>occur and arr[i] not in result:
                
                result.append(arr[i])
                
                
        result.sort()    
        return result
    
# Example usage:
solution = Solution()
print(solution.findMajority([3,2,3]))  # Output: [3]
# Problem: Majority Element II
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# Note: The algorithm should run in linear time and in O(1) space.
# Example 1:
# Input: nums = [3,2,3]
# Output: [3]
# Example 2:
# Input: nums = [1]
# Output: [1]
# Example 3:
# Input: nums = [1,2]
# Output: [1,2]
# Constraints:
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
# Approach:
# 1. Calculate the threshold as n/3.
# 2. Use a nested loop to count occurrences of each element.
# 3. If an element's count exceeds the threshold and it's not already in the result list, add it.
# 4. Sort the result list before returning.
# Time Complexity: O(n^2)
# Space Complexity: O(1) excluding the output list.  