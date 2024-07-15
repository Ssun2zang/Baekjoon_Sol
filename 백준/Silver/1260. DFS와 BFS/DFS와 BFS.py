import copy

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]
    
    def get_graph(self):
        return self.graph


n, m, start = map(int, input().split())
g = Graph()

# 그래프에 edge를 저장함
for i in range(m):
    u, v = map(int, input().split())
    g.add_edge(u, v)

if start not in g.get_graph().keys():
    print(start)
    print(start)
else:
    # DFS (깊이 우선 탐색)
    visited = []

    def dfs(s):
        visited.append(s)
        for temp in sorted(g.get_graph()[s]):
            if temp in visited:
                pass
            else:
                dfs(temp)   

    dfs(start)
    print(*visited)

    # BFS (넓이 우선 탐색)
    bfs_ans = []
    def bfs(s):
        queue = [s]
        bfs_ans.append(s)
        while queue:
            t = queue.pop(0)
            for temp in sorted(g.get_graph()[t]):
                if temp not in bfs_ans and temp:
                    queue.append(temp)
                    bfs_ans.append(temp)


    bfs(start)
    print(*bfs_ans)