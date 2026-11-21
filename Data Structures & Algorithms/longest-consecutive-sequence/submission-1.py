from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for num in numsSet:
            if num - 1 not in numsSet:
                current = num
                streak = 1

                while current + 1 in numsSet:
                    current += 1
                    streak += 1

                longest = max(longest, streak)
        return longest