for i in range(len(A)): #A bir liste
	j=i
	while j>0 and A[j]>A[j+1]:
		A[j-1],A[j]=A[j],A[j-1]
		j-=1
