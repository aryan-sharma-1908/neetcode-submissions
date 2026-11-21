class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        appended = set()
        result = []
        for i,ele in enumerate(strs):
            sublist = []
            if i in appended:
                continue
            else:
             sublist.append(ele)
             appended.add(i)
             if (i == (len(strs) - 1)): result.append(sublist)
            sortedEle = sorted(ele)
            for j in range(i+1,len(strs)):
                sortedOtherEle = sorted(strs[j])
                if(not (j in appended) and sortedEle == sortedOtherEle):
                    sublist.append(strs[j])
                    appended.add(j)
                if(j == len(strs) - 1):
                    result.append(sublist)
            
        return result        