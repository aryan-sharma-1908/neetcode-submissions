class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        withoutDuplicates = list(dict.fromkeys(nums))
        return withoutDuplicates != nums
        # correct answer as set is ordered
