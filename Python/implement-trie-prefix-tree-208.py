#https://leetcode.com/problems/implement-trie-prefix-tree/
#Level: Medium
#Time Complexity: O(n), n = len(word) for insert, search and startsWith
#Space Complexity: O(n), n = len(word) for insert, O(1) for search and startsWith



class TrieTree:

    def __init__(self):
        self.subTree: dict[str, TrieTree] = {}
        self.word = False

    def setSubTree(self, ch: str):
        if ch not in self.subTree:
            self.subTree[ch] = TrieTree()

    def getSubTree(self, ch: str) -> TrieTree | None:
        return self.subTree.get(ch)


class Trie:

    def __init__(self):
        self.trieTreeHead = TrieTree()

    def insert(self, word: str) -> None:
        tempHead = self.trieTreeHead

        for ch in word:
            tempHead.setSubTree(ch)
            tempHead = tempHead.getSubTree(ch)

        tempHead.word = True

    def search(self, word: str) -> bool:
        tempHead = self.trieTreeHead

        for ch in word:
            tempHead = tempHead.getSubTree(ch)
            if not tempHead:
                return False

        return tempHead.word

    def startsWith(self, prefix: str) -> bool:
        tempHead = self.trieTreeHead

        for ch in prefix:
            tempHead = tempHead.getSubTree(ch)
            if not tempHead:
                return False

        return True