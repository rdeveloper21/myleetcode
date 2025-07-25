'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''
from typing import List

'''
Intuition: By observation, we see that the first column of the original matrix is the reverse of the first 
row of the rotated matrix, so that’s why we transpose the matrix and then reverse each row, and since we 
are making changes in the matrix itself space complexity gets reduced to O(1).
'''

# Time O(N*N) + O(N*N).One O(N*N) is for transposing the matrix and the other is for reversing the matrix
# Space O(1)

def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    # logic for transpose of a square matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reversing each row of the matrix
    for i in range(n):
        matrix[i].reverse()

if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(arr)
    print("Rotated Image")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()