class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskfreq = Counter(tasks)
        heap = [-v for v in taskfreq.values()]
        heapq.heapify(heap)
        
        cooldown_queue = deque()
        time = 0
        
        while heap or cooldown_queue:
            time += 1
            
            if heap:
                count = heapq.heappop(heap) + 1
                if count != 0:
                    cooldown_queue.append([count, time + n])
            
            if cooldown_queue and cooldown_queue[0][1] == time:
                heapq.heappush(heap, cooldown_queue.popleft()[0])

        return time