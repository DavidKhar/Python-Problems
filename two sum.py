class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i]+nums[j]==target:
                    return(i, j)
        return('no pairs found!')
solution = Solution()
print(solution.twoSum([1, 5, 6, 2], 6))