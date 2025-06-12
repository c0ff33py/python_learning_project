class Solution:

    def twosun(self, nums: list[int], target: int) -> list[int]:
        nums = [2, 7, 11, 15]
        n = len(nums)
        for i in range(n):

            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


solution = Solution()
print(solution.twosun([2, 7, 11, 15], 9))
