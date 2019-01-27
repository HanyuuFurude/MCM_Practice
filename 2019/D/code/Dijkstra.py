class dijkstra:

    def __init__(self, graph):
        self.graphNode = {}
        for x in graph:
            self.graphNode[graph.list[x][0]][graph.list[x][1]] = graph.list[x]
            self.graphNode[graph.list[x][1]][graph.list[x][0]] = graph.list[x]




def cal(start, graph):
    n = len(graph)
    # print(n)
    costs = [float('inf') for _ in range(n)]
    costs[start] = 0
    parents = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    t = []
    while len(t) < n:
        minCost = float('inf')
        minNode = None
        for i in range(n):
            if not visited[i] and costs[i] < minCost:
                minCost = costs[i]
                minNode = i
        t.append(minNode)
        visited[minNode] = True

        for edge in graph[minNode]:
            if not visited[edge[0]] and minCost + edge[1] < costs[edge[0]]:
                costs[edge[0]] = minCost+edge[1]
                parents[edge[0]] = minNode
    return costs, parents
