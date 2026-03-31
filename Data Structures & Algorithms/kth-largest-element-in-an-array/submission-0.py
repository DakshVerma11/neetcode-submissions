class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=[]
        
        for num in nums:
            arr.append(-1*num)
        
        heapq.heapify(arr)

        for _ in range(k-1):
            heapq.heappop(arr)
        
        return -1*arr[0]