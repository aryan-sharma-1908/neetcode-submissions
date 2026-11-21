class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)        
        currentSum = 0
        for i in range(0,len(nums)):
            leftSum = currentSum
            currentSum += nums[i]
            rightSum = totalSum - currentSum
            if(leftSum == rightSum):
                return i

        return -1