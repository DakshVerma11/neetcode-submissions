class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxfreq = max(count.values())
        maxfreqtasks = list(count.values()).count(maxfreq)
        ans = (maxfreq - 1) * (n + 1) + maxfreqtasks
        
        return max(len(tasks), ans)