class Solution:
    def reorganizeString(self, s: str) -> str:
        charFreq=Counter(s)

        n=len(s)

        ans=['#']
        heap=[]
        for k,v in charFreq.items():
            heapq.heappush(heap,[-1*v,k])
            if 2*v>n+1:
                return ""  

        for i in range(n):
            temp=heapq.heappop(heap)
            if ans[-1]==temp[1]:
                temp2=heapq.heappop(heap)
                heapq.heappush(heap,temp)
                temp=temp2
            ans.append(temp[1])
            heapq.heappush(heap,[temp[0]+1,temp[1]])
        return ''.join(ans[1::])