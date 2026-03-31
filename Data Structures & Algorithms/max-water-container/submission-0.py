class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater=0
        i=0
        j=len(heights)-1
        while i<j:
            water=(j - i) * min(heights[i], heights[j])
            maxwater=max(maxwater,water)

            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1

        return maxwater 