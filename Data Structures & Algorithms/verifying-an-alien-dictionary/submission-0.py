class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx={}
        for i,v in enumerate(order):
            idx[v]=i
        
        for i in range(len(words)):
            word=words[i]
            cur=0
            for j in range(1001):
                if j<len(word):
                    cur+=idx[word[j]]
                cur*=27
            words[i]=cur
        #print(words)
        return words==sorted(words)
