class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        seen = {}
        for i,num2 in enumerate(nums2):
            seen[num2] = i
        
        for i,num1 in enumerate(nums1):
            j = seen[num1] + 1
            while j < len(nums2):
                if(num1 < nums2[j]):
                    result[i] = nums2[j]
                    break
                j += 1

        return result