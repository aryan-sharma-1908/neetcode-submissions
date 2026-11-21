class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(0,len(nums),1):
            for j in range(i+1,len(nums),1):
                for k in range(j+1,len(nums),1):
                    if(nums[j] + nums[k] == -nums[i]):
                        subList = []
                        subList.append(nums[i])
                        subList.append(nums[j])
                        subList.append(nums[k])
                        if(sorted(subList) not in result):
                            result.append(sorted(subList))
        return result