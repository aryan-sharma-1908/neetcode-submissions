class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r= 0,0

        while r < k - 1:
            r += 1
        diff = nums[-1] 
        while r < len(nums):
            mx = nums[r]
            mn = nums[l]
            l += 1
            r += 1
            diff = min(diff,mx - mn)

        return diff
