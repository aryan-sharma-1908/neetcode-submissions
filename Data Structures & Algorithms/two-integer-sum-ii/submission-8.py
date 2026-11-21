# Using Hashmap
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        map = defaultdict()
        for i,num in enumerate(numbers):
            map[num] = i

        for i,num in enumerate(numbers):
            if(target - num in map):
                return [i + 1, map[target - num] + 1]