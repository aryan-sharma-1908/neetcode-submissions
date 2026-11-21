class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalSum = len(nums) * (len(nums) + 1)//2
        numsSum = sum(nums)
        return totalSum - numsSum