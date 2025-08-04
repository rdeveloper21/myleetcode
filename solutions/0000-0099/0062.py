# Unique Paths
'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach 
the bottom-right corner.

Example:
Input: m = 3, n = 7
Output: 28

Input: m = 3, n = 2
Output: 3

Constraints:
1 <= m, n <= 100

'''

#Approach 1: The problem states that we can either move rightward or downward direction. So we recursively try out all the possible combinations.

def uniquePaths(m: int, n: int) -> int:
    def countPaths(i, j, n, m):
        if i == (n - 1) and j == (m - 1):
            return 1
        if i >= n or j >= m:
            return 0
        else:
            return countPaths(i + 1, j, n, m) + countPaths(i, j + 1, n, m)
        
    return countPaths(0, 0, m, n)

if __name__ == "__main__":
    totalCount = uniquePaths(3, 2)
    print("The total number of Unique Paths are ", totalCount)