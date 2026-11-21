class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n):
            j,k = i+1,n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    sub = [nums[i],nums[j],nums[k]]
                    if sub not in res:
                        res.append(sub) 
                    j += 1
                    k -= 1  
                elif s < 0:
                    j += 1
                else:
                    k -= 1

        return res
                
