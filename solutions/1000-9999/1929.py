# Concatenation of array
'''
Below are the 2 approaches for the solution
'''
from typing import *

class Solution:
    # Iteration One pass
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i, num in enumerate(nums):
            ans[i] = ans[i+n] = num
        return ans

    # Iteration Two pass
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
   