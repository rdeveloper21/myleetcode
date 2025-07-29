# Set Matrix Zeroes - In-place

'''
Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then
return the matrix.

'''

# Time O(2*(rows * columns))
# Space O(1)

def zeroMatrix(matrix):
    rows, columns = len(matrix), len(matrix[0])
    col0 = 1
    # step 1: Traverse the matrix and
    # mark 1st row & col accordingly:
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0:
                # mark i-th row:
                matrix[i][0] = 0
                # mark j-th column:
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0
    print("Value after step 1", matrix, end="\n")
    # Step 2: Mark with 0 from (1,1) to (rows-1, columns-1):
    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][j] != 0:
                # check for col & row:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
    print("Value after step 2", matrix, end="\n")
    #step 3: Finally mark the 1st col & then 1st row:
    if matrix[0][0] == 0:
        for j in range(columns):
            matrix[0][j] = 0
    print("Value after step 3.1", matrix, end="\n")
    if col0 == 0:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix


if __name__ == '__main__':
    nums = [[0,1,2,0],[3,4,5,2],[1,3,1,5],[3,4,5,6]]

    output = zeroMatrix(nums)

    print("Output matrix:", output)