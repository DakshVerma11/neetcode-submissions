class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #Kinda Dijkstra
        # Time O(m*n long(m*n))
        #Space O(m*n)
        #another option is binary search with dfs as we have to find the min max abs difference
        #also kruskal is another way
        ROWS = len(heights)
        COLS = len(heights[0])

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        minHeap = [(0, 0, 0)]
        visited = set()

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue

            if (r, c) == (ROWS - 1, COLS - 1):
                return diff

            visited.add((r, c))

            for dx, dy in directions:
                newR, newC = r + dx, c + dy
                if newR < 0 or newR >= ROWS or newC < 0 or newC >= COLS:
                    continue
                if (newR, newC) in visited:
                    continue
                newDiff = max(diff, abs(heights[newR][newC] - heights[r][c]))
                heapq.heappush(minHeap, (newDiff, newR, newC))

        return -1

