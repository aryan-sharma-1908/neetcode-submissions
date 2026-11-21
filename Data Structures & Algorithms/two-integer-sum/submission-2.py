class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, ele in enumerate(nums):
            otherEle = target - ele
            if otherEle in seen:
                return [seen.get(otherEle),i]
            seen[ele] = i
            