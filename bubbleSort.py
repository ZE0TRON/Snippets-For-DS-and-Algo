swapped=true
while swapped:
	swapped=false
	for i in range(len(A)):
		if A[i]>A[i+1]:
			A[i],A[i+1]=A[i+1],A[i]
			swapped=true
