





from typing import List
def maxArea(height: List[int]) -> int:
    n = len(height)
    left = 0
    right = n - 1
    res = 0

    while left< right:
        area = (right - left) * min(height[left], height[right])
        res = max(res, area)
        if height[left] < height[right]:
            left+=1
        else:
            right -= 1
    
    return res

if __name__ == "__main__":
    arr = [1,8,6,2,5,4,8,3,7]
    arr= [1,1]
    print(f"Max area: {maxArea(arr)}")
