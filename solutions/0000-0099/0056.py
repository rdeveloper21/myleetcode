'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

'''
# Time:  O(N*logN) + O(N), where N = the size of the given array.
# Space: O(N)
from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    n = len(intervals)

    # sort the given intervals:
    intervals.sort()
    ans = []
    for i in range(n):
        # if the current interval does not
        # lie in the last interval:
        if not ans or intervals[i][0] > ans[-1][1]:
            ans.append(intervals[i])
        # if the current interval
        # lies in the last interval:
        else:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
    return ans


if __name__ == '__main__':
    # intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals = [[1,4],[4,5]]
    ans = merge(intervals)
    print("The merged intervals are:")
    for it in ans:
        print(f"[{it[0]}, {it[1]}]", end=" ")
    print()

