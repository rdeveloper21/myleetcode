'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Example:
Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000

'''

def myPow(x: float, n: int) -> float:
    ans = 1.0
    for i in range(n):
        ans = ans * x
    return ans

if __name__ == "__main__":
    print(myPow(2, 10))