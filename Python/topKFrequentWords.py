#https://leetcode.com/problems/two-sum/
#level: Medium
#Time Complexity: O(nLog(k)), n = len(words), k = top k frequent words
#Space Complexity: O(n), n = len(words)


import heapq
from collections import Counter

class Word:
    def __init__(self, word: str, freq : int):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordsCounter = Counter(words)
        maxHeap = []
        heapq.heapify(maxHeap)

        
        for word, freq in wordsCounter.items():
            heapq.heappush(maxHeap, Word(word,freq))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        sortedMaxHeap = [heapq.heappop(maxHeap).word for _ in range(len(maxHeap))]
        return sortedMaxHeap[::-1]