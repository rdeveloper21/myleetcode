# Trapping water problem
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Input: height = [4,2,0,3,2,5]
Output: 9

'''
from typing import List

# Time O(N) because we are using 2 pointer approach.
# Space O(1) because we are not using anything extra.
def trap(height: List[int]) -> int:
    n = len(height)
    left = 0
    right = n - 1
    max_left = 0
    max_right = 0
    res = 0

    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= max_left:
                max_left = height[left]
            else:
                res += max_left - height[left]
            left += 1
        else: 
            if height[right] >= max_right:
                max_right = height[right]
            else:
                res += max_right - height[right]
            right -= 1
    return res

if __name__ == "__main__":
    # arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    arr = [4,2,0,3,2,5]
    print(f"The water that can be trapped is {trap(arr)}")