class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setOfNums = list(set(nums))
        return len(setOfNums) != len(nums)