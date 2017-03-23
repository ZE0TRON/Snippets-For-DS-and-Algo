def DFS(graph, u, v, travelled):
	if(u==v):
		return 1
	a=0
	for elem in graph[u]:
		if elem not in travelled:
			travelled.append(elem)
		a = a or DFS(graph, elem, v, travelled)
	return a
