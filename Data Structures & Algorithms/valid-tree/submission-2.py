class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n: return False

        if n == 1: return True
        
        adj = defaultdict(list)
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        explored = set()

        def dfs(node, par):
            if node in explored: return False

            explored.add(node)
            
            for child in adj[node]:
                if child == par: continue
                if not dfs(child, node): return False
            return True

        return dfs(0, -1) and len(explored) == n