class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = set()
        seen = set(nums2)
        
        for num1 in nums1:
            if(num1 in seen):
                intersection.add(num1)
        
        return list(intersection)