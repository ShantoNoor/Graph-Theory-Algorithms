t = {
	5: [4, 3],
	4: [1, -6],
	3: [0, 7, -4],
	1: [2, 9],
	7: [8]
}


s = 0
def sumOfLeafNodes(node):
	global s
	if t.get(node) == None:
		s+=node
		return


	for i in t[node]:
		sumOfLeafNodes(i)

	return s


print(sumOfLeafNodes(5))