g = [
	[], #0
	[2, 3], #1
	[2, 4, 4], #2
	[1, 2, 5], #3
	[3, 6], #4
	[6], #5
	[3], #6
]

n = len(g)
ind = [0]*n
outd = [0]*n
edge = 0
path = []

def calInOutDegree():
	global edge
	for i in range(n):
		for j in range(len(g[i])):
			outd[i] += 1
			ind[g[i][j]] += 1
			edge += 1


def graphHasEulerianPath():
	startNodeCount = 0
	endNodeCount = 0
	for i in range(n):
		if(ind[i]-outd[i] > 1 or outd[i] - ind[i] > 1):
			return False
		elif(ind[i]-outd[i] > 1):
			endNodeCount += 1
		elif(outd[i] - ind[i] > 1):
			startNodeCount += 1

	return ((startNodeCount == 0 and endNodeCount == 0) or
			(startNodeCount == 1 and endNodeCount == 1))


def findStartNode():
	start_node = 0
	for i 	in range(n):
		if(outd[i] - ind[i] == 1): return i
		if outd[i] > 0: start_node = i

	return start_node


def dfs(s):
	while outd[s] != 0:
		outd[s] -= 1
		next_node = g[s][outd[s]]
		dfs(next_node)

	path.append(s)


def findEulerianPath():
	calInOutDegree()
	if not graphHasEulerianPath():
		return []

	dfs(findStartNode())

	if len(path) == edge+1:
		path.reverse()
		return path

	return []


print(findEulerianPath())