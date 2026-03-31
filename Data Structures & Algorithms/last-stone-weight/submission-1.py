class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[]

        for stone in stones:
            maxHeap.append(-1*stone)
        
        heapq.heapify(maxHeap)

        while len(maxHeap)>1:
            stone1=-1*heapq.heappop(maxHeap)
            stone2=-1*heapq.heappop(maxHeap)
            if stone1==stone2:
                continue
            else:
                heapq.heappush(maxHeap,-1*(abs(stone1-stone2)))
        
        if maxHeap:
            return -1*maxHeap[0]
        return 0