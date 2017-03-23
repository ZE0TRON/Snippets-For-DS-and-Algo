def topological sort(g):
	”””Return a list of verticies of directed acyclic graph g in topological order.
	If graph g has a cycle, the result will be incomplete. ”””
 	topo = [ ]
	ready = [ ]
	incount = { }
	for u in g.vertices():
		# a list of vertices placed in topological order
		# list of vertices that have no remaining constraints # keep track of in-degree for each vertex
		incount[u] = g.degree(u, False) 
		if incount[u] == 0:
			ready.append(u) 
		while len(ready) > 0:
			u = ready.pop( ) 
			topo.append(u)
			for e in g.incident edges(u):
				v = e.opposite(u) incount[v] −= 1
				if incount[v] == 0:
					ready.append(v) 
	return topo
