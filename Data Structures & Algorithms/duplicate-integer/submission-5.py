class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = defaultdict(int)
        for num in nums:
            hash[num] += 1

        for num in nums:
            if(hash[num] > 1):
                return True
        
        return False