def floyd warshall(g):
	”””Return a new graph that is the transitive closure of g.”””
	closure = deepcopy(g) # imported from copy module verts = list(closure.vertices()) # make indexable list
	n = len(verts)
	for k in range(n):
		for i in range(n):
			# verify that edge (i,k) exists in the partial closure
			if i != k and closure.get edge(verts[i],verts[k]) is not None:
				for j in range(n):
					# verify that edge (k,j) exists in the partial closure
					if i != j != k and closure.get edge(verts[k],verts[j]) is not None:
						# if (i,j) not yet included, add it to the closure if closure.get edge(verts[i],verts[j]) is None:
						closure.insert edge(verts[i],verts[j]) return closure
