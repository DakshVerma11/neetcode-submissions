class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        inorder=[0]*numCourses

        for u,v in prerequisites:
            inorder[v]+=1
            adj[u].append(v)
        

        queue=deque()

        for i in range(numCourses):
            if inorder[i]==0:
                queue.append(i)
        done=0
        while queue:
            cur=queue.popleft()
            done+=1
            for neighbor in adj[cur]:
                inorder[neighbor]-=1
                if inorder[neighbor]==0:
                    queue.append(neighbor)
        return done==numCourses