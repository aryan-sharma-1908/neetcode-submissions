class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        seen = {num : i for i, num in enumerate(nums1)}
        stack = deque()
        
        i = 0
        for num in nums2:
            while len(stack) != 0 and stack[-1] < num:
                if stack[-1] not in seen:
                    stack.pop()
                    continue
                result[seen[stack.pop()]] = num
            stack.append(num)

        return result