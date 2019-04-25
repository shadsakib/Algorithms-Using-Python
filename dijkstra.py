import math, heapq

graph = {  0: {1:2, 3:5},
           1: {2:1, 1:4},
           2: {3:1},
           3: {},
           4: {2:3}
          }

dist = [math.inf for x in range(100)]

def dijkstra(s, totalVertex):

    dist[s] = 0
    pq = []
    heapq.heappush(pq, [s, dist[s]])

    while totalVertex>0:

        pair = heapq.heappop(pq)
        u = pair[0]

        adjList = graph[u]
        for v in adjList:
            if dist[v] > dist[u]+adjList[v]:
                dist[v] = dist[u]+adjList[v]
                heapq.heappush(pq, [v, dist[v]])

        totalVertex-=1

dijkstra(0, 5)

for i in range(5):
    s = "Cost[{0}] = {1}".format(i, dist[i])
    print(s)




