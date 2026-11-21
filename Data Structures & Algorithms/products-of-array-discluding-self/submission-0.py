class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
                continue
            product *= num
        
        for num in nums:
            if zeroCount > 1:
                result.append(0)
                continue
            if zeroCount == 1:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
                continue
            result.append(product // num)

        return result