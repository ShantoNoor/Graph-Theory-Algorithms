def treeCenters(t):
	n = len(t)
	degree = [0]*n
	leafs = []

	for i in range(n):
		degree[i] = len(t[i])

		if degree[i] == 0 or degree[i] == 1:
			leafs.append(i)
			degree[i] = 0

	count = len(leafs)
	while count < n:
		new_leafs = []
		for node in leafs:
			for neighbor in t[node]:
				degree[neighbor] -= 1
				if degree[neighbor] == 1:
					new_leafs.append(neighbor)

			degree[node] = 0

		count += len(new_leafs)
		leafs = new_leafs

	return leafs

if __name__ == "__main__":
	t = [
		[1],#0
		[0, 2],#1
		[1, 3, 6, 9],#2
		[2, 4, 5],#3
		[3],#4
		[3],#5
		[2, 7, 8],#6
		[6],#7
		[6],#8
		[2],#9
	]
	
	print(treeCenters(t))
