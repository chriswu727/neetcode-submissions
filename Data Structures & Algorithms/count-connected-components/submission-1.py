class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        cnt = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                cnt += 1
        return cnt
            
        
