class Solution:
    def sortedSquares(self, nums):
        ans = []
        i, j = 0, len(nums) - 1
        while i <= j:
            print(f"Iter:{i} ans: {ans}")
            a = nums[i] * nums[i]
            b = nums[j] * nums[j]
            if a > b:
                ans.append(a)
                i += 1
            else:
                ans.append(b)
                j -= 1

        print(f"Answer: {ans}")
        return ans[::-1]
    
oops = Solution()
print(oops.sortedSquares([-10, -5, -2, 0, 1, 4, 8]))