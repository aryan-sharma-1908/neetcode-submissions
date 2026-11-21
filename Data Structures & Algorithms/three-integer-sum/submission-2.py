class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        setOfNums = set()
        for num in nums:
            setOfNums.add(num)
        
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                thirdEle = -(nums[i] + nums[j])
                if(thirdEle in setOfNums and nums.index(thirdEle) != i and nums.index(thirdEle) != j):
                    subList = []
                    subList.append(nums[i])
                    subList.append(nums[j])
                    subList.append(-(nums[i] + nums[j]))
                    if(sorted(subList) not in result):
                        result.append(sorted(subList))
            
        return result