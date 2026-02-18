#https://leetcode.com/problems/sort-characters-by-frequency/
#Level: Medium
#Time Complexity: O(n), n = len(nums)
#Space Complexity: O(n), n = len(nums)



from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        freqDic = {}
        sLen = len(s)
        freqBuckets = defaultdict(list)
        i = sLen
        sFreq = []


        for j in range(sLen):
            freqDic[s[j]] = freqDic.get(s[j],0) + 1

        for letter, freq in freqDic.items():
            freqBuckets[freq].append(letter)
        
        for freq in range(sLen, 0, -1):
            for char in freqBuckets[freq]:
                sFreq.append(char * freq)



        return "".join(sFreq)

        


        