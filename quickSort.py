def quickSort(A,lo,hi):
	if lo<hi:
		p=partition(A,lo,hi)
		quickSort(A,lo,p-1)
		quickSort(A,p+1,hi)
		return A
def	partition(A,lo,hi):
	pivot=A[hi]
	i=lo-1
	for i in range(lo,hi):
		if[j]<=pivot:
			j=i+1
		A[j],A[i]=A[i],A[j]
	A[i+1],A[i]=A[i],A[i+1]
	return i+1
