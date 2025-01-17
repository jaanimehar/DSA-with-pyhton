def next_permutation(nums):
    """
    Modifies nums in-place to the next permutation.
    """
    # Find the first index 'i' such that nums[i] < nums[i + 1] from the end
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Find the first index 'j' such that nums[j] > nums[i] from the end
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse the sequence from i + 1 to the end
    nums[i + 1:] = reversed(nums[i + 1:])
    
# Example usage
nums = [1, 2, 3]
next_permutation(nums)
print(nums)  # Output: [1,3,2]