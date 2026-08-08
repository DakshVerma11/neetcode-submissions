class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}

        for frm, to, price in flights:
            adj[frm].append((to, price))

        minHeap = [(0, src, 0)]  # cost, node, edges

        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        while minHeap:
            curCost, curNode, curEdges = heapq.heappop(minHeap)

            if curNode == dst:
                return curCost

            if curEdges == k + 1:
                continue

            if curCost > dist[curNode][curEdges]:
                continue

            for neighborNode, price in adj[curNode]:
                newCost = curCost + price
                newEdges = curEdges + 1

                if newCost < dist[neighborNode][newEdges]:
                    dist[neighborNode][newEdges] = newCost
                    heapq.heappush(
                        minHeap,
                        (newCost, neighborNode, newEdges)
                    )

        return -1
