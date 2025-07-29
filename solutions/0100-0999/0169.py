'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than 
⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example:
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''
from typing import List
# Time : O(N2), where N = size of the given array. 
# Space: O(1)
def majorityElement(nums: List[int]) -> int:
    n = len(nums) # Size of the given array
    
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] == nums[i]:
                count +=1
        
        if count > (n // 2):
            return nums[i]
        
    return -1 



# 2nd Approach
# Use a better data structure to reduce the number of look-up operations and hence the time complexity. 
# Use a hashmap and store as (key, value) pairs. (Can also use frequency array based on the size of nums) 
# Here the key will be the element of the array and the value will be the number of times it occurs. 

from collections import Counter
# Time: O(N*logN) + O(N), where N = size of the given array.
# Space: O(N) as we are using a map data structure.
def new_majorityElement(arr):
    # Size of the given array
    n = len(arr)

    # Count the occurrences of each element using Counter
    counter = Counter(arr)

    # Searching for the majority element
    for num, count in counter.items():
        if count > (n // 2):
            return num

    return -1


# Third Approach - Boyer-Moore’s Voting Algorithm
# Basically, we are trying to keep track of the occurrences of the majority element and minority elements dynamically. 

# Time O(N) + O(N), where N = size of the given array.
# Space: O(1)
def third_new_majorityElement(arr):
    # Size of the given array
    n = len(arr)
    count = 0 # Count
    element = None  # Element
    # Applying the algorithm
    for i in range(n):
        if count == 0:
            count = 1
            element = arr[i]
        elif arr[i] == element:
            count += 1
        elif arr[i] != element:
            count -= 1

    # Checking if the stored element is the majority element
    cnt1 = 0
    for i in range(n):
        if arr[i] == element:
            cnt1 += 1
    if cnt1 > (n / 2):
        return element
    return -1

if __name__ == '__main__':
    # arr = [3,2,3]
    arr = [2,2,1,1,1,2,2]
    output = third_new_majorityElement(arr)
    print("Following element is the majority element:", output)