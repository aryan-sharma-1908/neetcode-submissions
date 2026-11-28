class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        values = []
        i1,i2 = 0,0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                values.append(nums1[i1])
                i1 += 1
            else:
                values.append(nums2[i2])
                i2 += 1

        while i1 < len(nums1):
            values.append(nums1[i1])
            i1 += 1
        
        while i2 < len(nums2):
            values.append(nums2[i2])
            i2 += 1
        median = values[len(values)//2] * 1.0 if len(values) % 2 != 0 else (values[len(values)//2] + values[len(values)//2 - 1]) / 2
        return median