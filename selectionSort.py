for i in range(len(A)): #A bir liste
	imin=i
	minv=float("-inf")
	for j in range(1,len(A)):
		if A[j]<minv:
			minv=A[i]
			j=imin
	A[j],A[imin]=A[imin],A[j]
