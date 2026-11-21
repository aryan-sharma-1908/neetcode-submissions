class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        if(nums[0] < nums[len(nums) - 1]):
            return nums[0]
        s = 0
        e = len(nums) - 1
        while s < e:
            m = int(s + (e - s)/2)
            if(nums[m] < nums[e]):
                e = m
            elif(nums[m] > nums[e]):
                s = m + 1
        return nums[s]