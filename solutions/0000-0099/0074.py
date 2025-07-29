'''
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''
from typing import List


# Time: O(n + log(m)), where N = given row number, M = given column number
# Space : O(1)
def BinarySearch(matrix, target):
    n = len(matrix)
    low, high = 0, n-1

    while low < high:
        mid = (low + high) // 2
        if matrix[mid] == target:
            return True
        elif target > matrix[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        if matrix[i][0] <= target <= matrix[i][m - 1]:
            return BinarySearch(matrix[i], target)
    return False







# Time: O(log(m * n)), where N = given row number, M = given column number
# (We are applying binary search on the imaginary 1D array of size NxM)
# Space : O(1)
def new_searchMatrix(matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    low, high = 0, (n*m) - 1
    while low < high:
        mid = (low + high ) // 2 
        row = mid // m
        col = mid % m
        if matrix[row][col] == target:
            return True
        elif target > matrix[row][col]:
            low = mid + 1
        else:
            high = mid - 1
    return False


if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    output = new_searchMatrix(matrix=matrix, target=target)
    print("Status of target in matrix: ", output)
