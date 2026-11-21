class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        e = len(numbers) - 1
        while (numbers[s] + numbers[e] != target):
            sum = numbers[s] + numbers[e]
            if(sum > target):
                e -= 1
            else:
                s += 1
        return [s+1,e+1]