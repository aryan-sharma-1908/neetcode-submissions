class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = []
        prefixSum.append(nums[0])

        for i in range(1,len(nums)):
            prefixSum.append(nums[i] + prefixSum[-1])

        if(prefixSum[len(nums) - 1] - prefixSum[0] == 0):
            return 0
        
        if(prefixSum[len(nums) - 2] == 0):
            return len(nums) - 1

        for i in range(1,len(nums)):
            leftSum = prefixSum[i - 1]
            rightSum = prefixSum[len(nums) - 1] - prefixSum[i]
            if(leftSum == rightSum):
                return i

        return -1