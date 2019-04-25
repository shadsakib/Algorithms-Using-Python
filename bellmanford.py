import math

graph = {  0: {1:2, 3:5},
           1: {2:1, 3:-4,},
           2: {3:1},
           3: {},
           4: {2:3}
        }

dist = [math.inf for x in range(100)]

def bellmanford(s, n):
    dist[s] = 0
    for i in range(n-1):
        for u in graph:
            for v in graph[u]:
                if dist[v] > dist[u]+ graph[u][v]:
                    dist[v] = dist[u]+graph[u][v]
    for i in range(n):
        for v in graph[i]:
            if dist[v] > dist[i] +graph[i][v]:
                return False

    return True

if bellmanford(0, 5) == False:
    print("Negative Cycle")
    quit()

for i in range(5):
    print("cost[{0}] = {1}".format(i,dist[i]))

