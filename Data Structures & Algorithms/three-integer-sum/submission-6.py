class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, num in enumerate(nums):
            target = -num
            s = i + 1
            e = len(nums) - 1
            while s < e:
                if (nums[s] + nums[e] == target and [nums[i],nums[s],nums[e]] not in result):
                    result.append([nums[i], nums[s], nums[e]])
                    s += 1
                    e -= 1
                    continue
                elif (nums[s] + nums[e] < target):
                    s += 1
                else:
                    e -= 1
        return result