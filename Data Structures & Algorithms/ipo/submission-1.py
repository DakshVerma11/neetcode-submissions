class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n=len(profits)
        heap=[]
        res=0
        for i in range(n):
            heapq.heappush(heap,[-1*profits[i],capital[i]])
        
        
        for _ in range(k):

            temp=[]
            temp.append(heapq.heappop(heap))
            while heap and temp[-1][1]>w:
                temp.append(heapq.heappop(heap))
            
            if temp[-1][1]>w:
                break
            
            w+=-1* temp[-1][0]
            temp.pop()
            for i in temp:
                heapq.heappush(heap,i)



        return w