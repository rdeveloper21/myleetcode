'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and using only constant extra space.
Example:
Input: nums = [1,3,4,2,2]
Output: 2

Input: nums = [3,3,3,3,3]
Output: 3
'''
from typing import List


'''
Take a frequency array of size N+1 and initialize it to 0. Now traverse through the array 
and if the frequency of the element is 0 increase it by 1, else if the frequency is not 0 
then that element is the required answer.
'''
# Time O(n)
# Space O(n)

def findDuplicate(nums: List[int]) -> int:
    n = len(nums)
    freq = [0] * (n + 1)
    print(freq)
    for i in range(n):
        print(f"{i}: {freq}")
        if freq[nums[i]] == 0:
            freq[nums[i]] = 1
        else:
            return nums[i]
    return 0

if __name__ == "__main__":
    arr = [1, 3, 4, 2, 3]
    # arr = [3,3,3,3,3]
    print("The duplicate element is ", findDuplicate(arr))