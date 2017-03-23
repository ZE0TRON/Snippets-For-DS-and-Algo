def mergeSort(A):
	if len(A)<=1:
		return A
	left=[]
	right=[]
	for i in range(len(A)):
		x=m[i]
		if i<len(A)/2:
			left.append(x)
		else:
			right.append(x)
	left=mergeSort(left)
	right=mergeSort(right)
	return merge(left,right)
def merge(left,right):
	result=[]
	while len(left)>0 and len(right)>0:
		if left[0]<=right[0]:
			result.append(left[0])
			left.pop(0)
		else:
			result.append(right[0])
			right.pop(0)
	while len(left)>0:
		result.append(left[0])
		left.pop(0)
	while len(right)>0:
		result.append(right[0])
		right.pop(0)
	return result
