'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.

'''
# Time O(n)
# Space O(1)
from typing import List
import sys 

def maxSubArray(nums: List[int]) -> int:
        n = len(nums)
        maxi = -sys.maxsize-1
        sum = 0
        ansstart = -1
        ansend = -1
        for val in range(n):
            if sum == 0:
                start = val
            sum += nums[val]

            if sum < 0:
                sum = 0

            if sum > maxi:
                maxi = sum
                ansstart = start
                ansend = val
        # print(ansstart)
        # print(ansend)
        result_array = []
        for value in range(ansstart, ansend):
             result_array.append(nums[value])

        print(result_array)
        return maxi

if __name__ == "__main__":
    A = [-2,1,-3,4,-1,2,1,-5,4] 
    ans = maxSubArray(A)

    print("max sum is:", ans)


# More optimized solution

import sys
from typing import List

def maxSubArray(nums: List[int]) -> int:
    n = len(nums)
    maxi = -sys.maxsize - 1
    current_sum = 0
    start = 0
    ansstart = -1
    ansend = -1

    for i in range(n):
        if current_sum == 0:
            start = i
        
        current_sum += nums[i]

        if current_sum > maxi:
            maxi = current_sum
            ansstart = start
            ansend = i

        if current_sum < 0:
            current_sum = 0

    # Just print the indices instead of storing the subarray
    if ansstart != -1 and ansend != -1:
        print("Max subarray is from index", ansstart, "to", ansend)
        print("Corresponding subarray:", nums[ansstart:ansend+1])  # Optional: for debug only

    return maxi
