class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setOfNums = {x for x in nums}
        return len(setOfNums) != len(nums)

