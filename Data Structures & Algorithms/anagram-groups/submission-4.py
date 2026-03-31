class Solution(object):
         
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list)
        for s in strs:
            count=[0]*26
            for i in s.lower():
                count[ord(i)-ord('a')]+=1
            ans[tuple(count)].append(s)
        return list(ans.values())

