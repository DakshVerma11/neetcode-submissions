class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tcount=defaultdict(int)
        res=" "*(len(s)+1)
        for i in t:
            tcount[i]+=1
 
        scount=defaultdict(int)
        l=0
        while l<len(s) and  s[l] not in tcount :
            l+=1
        
        for r in range(l,len(s)):
            if s[r] in tcount:
                scount[s[r]]+=1
            print(l,r)
            


            while l<r and (s[l] not in tcount or scount[s[l]]>tcount[s[l]]):
                if s[l] in tcount:
                    scount[s[l]]-=1
                l+=1

            if r-l+1<=len(res):
                valid = True
                for k,v in tcount.items():
                    if scount[k]<v:
                        valid=False        
                
                if valid:
                    res=s[l:r+1]
                        
        #print(tcount)
        #print(scount)
        return res if len(res)<=len(s) else ""
            
            
