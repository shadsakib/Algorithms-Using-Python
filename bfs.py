import queue

def bfs(s):
    q = queue.Queue()
    visited[s] = 1
    q.put(s)

    while (q.empty() != True):
        u = q.get()
        for v in graph[u]:
            if visited[v] == 0:
                visited[v] = 1
                cost[v] = cost[u] + 1
                q.put(v)

n = int(input())
e = int(input())

cost = [0 for i in range(n)]
visited = [0 for i in range(n)]
graph = [[] for i in range(n)]

for i in range(e):
    n1, n2 = [int(j) for j in input().split()]
    graph[n1].append(n2)

s = int(input())
e = int(input())

bfs(s)
print(cost[e])
