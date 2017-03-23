from collections import defaultdict, deque


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited


t = int(input().strip())
for a0 in range(t):
    g = Graph()
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    for i in range(1, n + 1):
        g.add_node(i)
    for a1 in range(m):
        x, y, a = input().strip().split(' ')
        x, y, a = [int(x), int(y), int(a)]
        if x not in g.edges[y]:
            g.add_edge(x,y,a)
            g.add_edge(y,x,a)
        else:
            if g.distances[(x,y)]>a:
                g.distances[x,y]=a
                g.distances[(y,x)]=a
    startpoint = int(input().strip())
    answer = dijkstra(g, startpoint)
    aa = []
    for i in range(1, n + 1):
        if i != startpoint:
            try:
                aa.append(str(answer[i]))
            except:
                aa.append("-1")
    print(" ".join(aa))
