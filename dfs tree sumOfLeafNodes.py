t = {
	5: [4, 3],
	4: [1, -6],
	3: [0, 7, -4],
	1: [2, 9],
	7: [8]
}


def sumOfLeafNodes(node):
	if t.get(node) == None:
		return node

	s = 0
	for i in t[node]:
		s += sumOfLeafNodes(i)

	return s


print(sumOfLeafNodes(5))