import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        projects = list(zip(capital, profits))
        heapq.heapify(projects)
        available_projects = []
        
        for _ in range(k):
            while projects and projects[0][0] <= w:
                capital_req, profit = heapq.heappop(projects)
                heapq.heappush(available_projects, -profit)
            
            if not available_projects:
                break
            
            w -= heapq.heappop(available_projects)
        
        return w
