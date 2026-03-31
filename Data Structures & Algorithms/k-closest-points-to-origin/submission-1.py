class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distPoint=defaultdict(list)
        dist=[]
        for point in points:
            x=point[0]
            y=point[1]

            distance= math.sqrt(x*x+y*y)
            dist.append(distance)
            distPoint[distance].append(point)
        heapq.heapify(dist)
        res=[]

        while len(res)<k:
            shortestdist=heapq.heappop(dist)

            listOfPoints = distPoint[shortestdist]

            while listOfPoints and len(res)<k:
                i=listOfPoints.pop()
                res.append(i)
            
        return res
