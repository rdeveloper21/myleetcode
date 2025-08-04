

from typing import List
def twoSum(nums, target):
    num_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index
    return [] # Or raise an exception if no solution exists

if __name__ == '__main__':
    
    nums = [2,7,11,15] 
    target = 22
    print(f"Two sum value: {twoSum(nums, target)}")