'''
You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2].
Each integer appears exactly once except a which appears twice and b which is missing.
The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

Example:
Input: grid = [[1,3],[2,2]]
Output: [2,4]
Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].

Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
Output: [9,5]
Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].
'''
from typing import List
def findMissingAndRepeatedValues(grid: List[List[int]]) -> List[int]:
    n = len(grid)
    m = len(grid[0])
    hash = [0] * ((n * n) + 1)

    for i in range(n):
        for j in range(m):
            hash[grid[i][j]] += 1

    repeating = -1 
    missing = -1
    for i in range(1, ((n * n) + 1)):
        if hash[i] == 2:
            repeating = i
        elif hash[i] == 0:
            missing = i
        
        if repeating != -1 and missing != -1:
            break
    return [repeating, missing]

if __name__ == '__main__':
    grid = [[1,3],[2,2]]
    result = findMissingAndRepeatedValues(grid)
    print(f"Following is the repeating and missing values: {result}")