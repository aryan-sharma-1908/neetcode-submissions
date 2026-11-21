class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l,r, total, result = 0,0,0,0

        while r < k:
            total += arr[r]
            r += 1
        
        while r < len(arr):
            avg = total / k
            if(avg >= threshold):
                result += 1
            total += -arr[l] + arr[r]
            l += 1
            r += 1
        
        if total / k >= threshold:
            result += 1
        return result