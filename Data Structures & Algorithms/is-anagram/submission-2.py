class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq=Counter(s)
        key=set(s)
        for i in t:
            if i not in s:
                return False
            freq[i]-=1

        for key,values in freq.items():
            if values!=0:
                return False
        return True