from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjency list
        adj = [[] for _ in range(numCourses)]
        ind = [0] * numCourses # calculate indegree of every course
        for a , b in prerequisites :
            adj[b].append(a)
            ind[a] += 1
        q = deque()
        for i in range(numCourses):
            if ind[i] == 0 :
                q.append(i)
        count = 0 
        while q:
            node = q.popleft()
            count += 1
            for nei in adj[node]:
                ind[nei] -= 1
                if ind[nei] == 0 :
                    q.append(nei)
        return count == numCourses


