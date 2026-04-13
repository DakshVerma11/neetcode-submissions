class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for w in dictionary:
            trie.addWord(w)
        N=  len(s)
        dp = {N: 0}

        def backtrack(i):
            if i in dp:
                return dp[i]
            res = 1 + backtrack(i + 1)
            curr = trie.root
            for j in range(i, N):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.isWord:
                    res = min(res, backtrack(j + 1))

            dp[i] = res
            return res

        return backtrack(0)