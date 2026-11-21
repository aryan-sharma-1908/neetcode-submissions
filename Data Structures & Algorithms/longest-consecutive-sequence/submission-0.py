from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        hashTable = {}
        for num in sortedNums:
            if(num not in hashTable):
                hashTable[num] = 1
                if(num - 1 in hashTable):
                    hashTable[num] += hashTable[num - 1]
        maxConsecutive = 0
        for value in hashTable.values():
            if(value > maxConsecutive):
                maxConsecutive = value
        return maxConsecutive
