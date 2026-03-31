class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        maxfreq=0
        for x in nums:
            freq[x] += 1
            if freq[x] > maxfreq:
                maxfreq = freq[x]


        buckets = [[] for _ in range(maxfreq + 1)]


        for num,count in freq.items():
            buckets[count].append(num)

        res=[]
        for i in range(maxfreq,0,-1):
            if buckets[i]:
                res.extend(buckets[i])
            if len(res)>=k:
                return res[:k]
        return res[:k]