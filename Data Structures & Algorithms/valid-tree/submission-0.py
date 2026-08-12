class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        visited = set()
        def dfs(node, parenent):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, node)

        dfs(0, None)
        return len(visited) == n 
