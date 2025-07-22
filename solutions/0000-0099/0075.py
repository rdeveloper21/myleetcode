'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

This problem is a variation of the popular Dutch National flag algorithm. 

'''
# Time O(n)
# Space O(1)
from typing import List
def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

        


arr = [0, 2, 1, 2, 0, 1, 2, 0, 1, 1, 0, 2]
sortColors(arr)
print("After sorting:")
for num in arr:
    print(num, end=" ")
print()
                