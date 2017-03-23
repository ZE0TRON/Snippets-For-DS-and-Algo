def BFS(graph, start, end, travelled):
	q=[start]
	while len(q)!=0:
		current = q.pop(0)
		if current==end:
			return 1
		for elem in graph[current]:
			if elem not in travelled:
				q.append(elem)
				travelled.append(elem)
	return 0
