'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example:
Input: nums = [3,2,3]
Output: [3]

Input: nums = [1]
Output: [1]

Input: nums = [1,2]
Output: [1,2]

'''
from typing import List
def majorityElement(nums: List[int]) -> List[int]: 
    # Size of the given array
    n = len(nums)

    cnt1, cnt2 = 0, 0
    el1, el2 = None, None 
    
    # Applying the algorithm
    for i in range(n):
        if cnt1 == 0 and el2 != nums[i]:
            cnt1 = 1
            el1 = nums[i]
        elif cnt2 == 0 and el1 != nums[i]:
            cnt2 = 1
            el2 = nums[i]
        elif nums[i] == el1:
            cnt1 +=1
        elif nums[i] == el2:
            cnt2 +=1
        else:
            cnt1 -=1
            cnt2 -=1

    # Checking if the stored element is the majority element
    ls = []
    cnt1, cnt2 = 0, 0
    for i in range(n):
        if nums[i] == el1:
            cnt1 += 1
        elif nums[i] == el2:
            cnt2 += 1

    mini = int(n/3) + 1

    if cnt1 >= mini:
        ls.append(el1)
    if cnt2 >= mini:
        ls.append(el2)
    
    return ls

if __name__ == '__main__':
    # arr = [3,2,3]
    # arr = [2,2,1,1,1,2,2]
    # arr = [1]
    arr = [1,2]
    output = majorityElement(arr)
    print("Following element is the majority element:", output)