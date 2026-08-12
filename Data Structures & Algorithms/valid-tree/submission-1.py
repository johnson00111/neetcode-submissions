class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return False
            else:
                parent[root_a] = root_b
                return True

        for a, b in edges:
            if not union(a, b):
                return False

        key = find(0)
        for i in range(1, n):
            if find(i) != key:
                return False
        return True