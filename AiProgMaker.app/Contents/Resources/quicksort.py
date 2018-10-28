# Created by Aish Gupta on 05/03/18
# Quicksort

def sort(A,p,r):
	if p < r:
		q = partition(A,p,r)
		sort(A,p,q-1)
		sort(A,q+1,r)
	return A

def partition(A,p,r):
	x = A[r]
	i = p-1
	for j in range(p,r):
		if A[j] <= x:
			i += 1
			A[i],A[j] = A[j],A[i]
	A[i+1],A[r] = A[r],A[i+1]
	return i+1


unsorted_list = []
n = input('enter the size of the list')
print('enter the list')

for i in range(0,n):
	unsorted_list.append(input())

print('the unsorted list is	' + str(unsorted_list))
print('the sorted list is' + str(sort(unsorted_list,0,len(unsorted_list)-1)))