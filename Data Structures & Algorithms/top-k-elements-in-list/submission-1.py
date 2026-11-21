from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = defaultdict(int)
        maxCount = 0
        for num in nums:
            count[num] += 1
            if(count[num] > maxCount):
                maxCount = count[num]

        freq = sorted(count.values(),reverse=True)
        minOfMaxAllowedFreq = freq[k - 1]

        for key,value in count.items():
            if(value >= minOfMaxAllowedFreq and len(result) <= k):
                result.append(key)
        
        return result
        