class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        
        for j in range(len(s)):
            setchar=set()
            count=0
            i=j
            while i<len(s) and s[i] not in setchar:
                setchar.add(s[i])
                count+=1
                i+=1
            maxlen=max(count,maxlen)
        return maxlen