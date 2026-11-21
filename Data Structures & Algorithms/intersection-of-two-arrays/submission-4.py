class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = set()
        hash = defaultdict()
        for num2 in nums2:
            hash[num2] = True
        
        for num1 in nums1:
            if(num1 in hash):
                intersection.add(num1)
        
        return list(intersection)