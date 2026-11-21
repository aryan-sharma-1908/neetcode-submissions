class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums2.sort()
        for num1 in nums1:
            start = 0
            end = len(nums2) - 1
            while start <= end:
                mid = start + (end - start)//2
                if(nums2[mid] == num1 and num1 not in intersection):
                    intersection.append(num1)
                    break
                elif(nums2[mid] < num1):
                    start = mid + 1
                else:
                    end = mid - 1
        return intersection