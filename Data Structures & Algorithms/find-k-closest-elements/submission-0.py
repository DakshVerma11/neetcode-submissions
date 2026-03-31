class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return sorted(arr)

        diff = []
        for i in range(len(arr)):
            diff.append((abs(x - arr[i]), arr[i]))
        diff.sort()
        result=[]
        for i in range(k):
            result.append(diff[i][1])
        result.sort()
        return result
