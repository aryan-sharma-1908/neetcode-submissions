class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        left_product = []
        left = 1
        right_product = []
        right = 1
        for i in range(len(nums)):
            if i == 0:
                left_product.append(1)
                continue
            left = left * nums[i-1]
            left_product.append(left)
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right_product.append(1)
                continue
            right = right * nums[i+1]
            right_product = [right] + right_product

        for i in range(len(nums)):
            result.append(left_product[i] * right_product[i])
        
        return result