class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        for i in nums:
            freq[i]+=1

        values=sorted(freq.values(), reverse=True)
        target=values[k-1]
        res=[]
        for k,v in freq.items():
            if v>=target:
                res.append(k)

        return res