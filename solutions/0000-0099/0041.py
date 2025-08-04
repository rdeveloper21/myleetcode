# First Missing Positive
'''
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
Example:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

'''
from typing import List
def firstMissingPositive(nums: List[int]) -> int:
    n = len(nums)
    print(nums)
    for i in range(n):
        while (1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]):
            # Swap nums[i] with nums[nums[i] - 1]
            correct_idx = nums[i] - 1
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
    print(f"Step 2{nums}")
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == '__main__':
    nums = [7,8,9,11,12]
    # nums = [3,4,-1,1]
    # nums = [1,2,0]
    result = firstMissingPositive(nums)
    print(f"Following is the first missing positive integer: {result}")