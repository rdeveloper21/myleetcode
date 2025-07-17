# Pascal Triangle

'''
Problem Statement: This problem has 3 variations. They are stated below:
In Pascal’s triangle, each number is the sum of the two numbers directly above it.
'''

# Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.
# O(c), where c = given column number.
def nCr(n, r):
    res = 1

    # Calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1) 

    return res

def PascalTriangle(r, c): 
    element = nCr(r-1, c-1)
    return element

if __name__ == '__main__':
    r = 5 # row number
    c = 3 # col number
    element = PascalTriangle(r, c)
    print(f"The element at position (r,c) is: {element}")



# Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.
# O(n*r)
def nCr(n, r):
    res = 1
    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res

def pascalTriangle(n):
    # printing the entire row n:
    for c in range(1, n+1):
        print(nCr(n-1, c-1), end=" ")
    print()

if __name__ == '__main__':
    n = 5
    pascalTriangle(n)



# Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.
# O(n2), where n = number of rows(given)
from typing import *

def generateRow(row):
    ans = 1
    ansRow = [1] #inserting the 1st element
    
    #calculate the rest of the elements:
    for col in range(1, row):
        ans *= (row - col)
        ans //= col
        ansRow.append(ans)
    return ansRow

def pascalTriangle(n : int) -> List[List[int]]:
    ans = []
    
    #store the entire pascal's triangle:
    for row in range(1, n+1):
        ans.append(generateRow(row))
    return ans

if __name__ == '__main__':
    n = 5
    ans = pascalTriangle(n)
    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()