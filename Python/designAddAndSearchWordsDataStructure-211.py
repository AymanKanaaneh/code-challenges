#https://leetcode.com/problems/design-add-and-search-words-data-structure
#Level: Medium
#Time Complexity: O(n), n = len(word) for addWord, O(m) for search, m = len(word) where word is the input to search
#Space Complexity: O(n), n = len(word) for addWord, O(m) for search, m = len(word) where word is the input to search


class TrieTree:

    def __init__(self):
        self.subTree: dict[str, TrieTree] = {}
        self.word = False
    
    def setSubTree(self, ch: str):
        if ch not in self.subTree:
            self.subTree[ch] = TrieTree()

    def getSubTree(self, ch: str) -> TrieTree | None:
        return self.subTree.get(ch)


class WordDictionary:

    def __init__(self):
        self.trieTreeHead = TrieTree()
        

    def addWord(self, word: str) -> None:
        tempHead = self.trieTreeHead

        for ch in word:
            tempHead.setSubTree(ch)
            tempHead = tempHead.getSubTree(ch)

        tempHead.word = True

    def search(self, word: str) -> bool:
        tempHead = self.trieTreeHead
        i = 0
        return self.searchHelp(tempHead, i, word)

    def searchHelp(self, tempHead, i, word):

        while i < len(word):

            ch = word[i]
            chrs = list(tempHead.subTree.keys())

            if ch == ".":
                j = 0
                while j < len(chrs):
                    nextNode = tempHead.getSubTree(chrs[j])
                    if self.searchHelp(nextNode, i + 1, word):
                        return True
                    j += 1
                return False
            else:
                tempHead = tempHead.getSubTree(ch)
                if not tempHead:
                    return False

            i += 1

        return tempHead.word



        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)